package com.TSreamProducers;

import com.TSreamProducers.model.Tweet;
import com.google.gson.Gson;
import com.twitter.hbc.ClientBuilder;
import com.twitter.hbc.core.Client;
import com.twitter.hbc.core.Constants;
import com.twitter.hbc.core.endpoint.StatusesFilterEndpoint;
import com.twitter.hbc.core.processor.StringDelimitedProcessor;
import com.twitter.hbc.httpclient.auth.Authentication;
import com.twitter.hbc.httpclient.auth.OAuth1;
import org.apache.kafka.clients.producer.*;
import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.common.serialization.LongSerializer;
import org.apache.kafka.common.serialization.StringSerializer;

import java.io.IOException;
import java.util.Collections;
import java.util.Properties;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class TProducer extends Producer{

    private Client client;
    private BlockingQueue<String> queue;
    private Gson gson;
    private Callback callback;

    public static final String CONSUMER_KEY = "wIav6v1npRTOcT42mSDgfTFHO";
    public static final String CONSUMER_SECRET = "JVLymntWbpiX6p2BexrrHTyn0kevWXOQgAaniB79U7n9WZ9ksx";
    public static final String ACCESS_TOKEN = "89109124-UC0ehEN72KV9t92KiO0k9l1cHwxMeaTVZfBGuCems";
    public static final String TOKEN_SECRET = "kBXM3DDhGV89QXsaq9mY9sCgDBHorGg2bKFyd69uU3FHC";
    public static final String HASHTAG = "#a";


    public TProducer() {

        Authentication authentication = new OAuth1(
                CONSUMER_KEY,
                CONSUMER_SECRET,
                ACCESS_TOKEN,
                TOKEN_SECRET);

        // filter by topic
        StatusesFilterEndpoint endpoint = new StatusesFilterEndpoint();
        endpoint.trackTerms(Collections.singletonList(HASHTAG));
        endpoint.filterLevel(Constants.FilterLevel.Medium);

        queue = new LinkedBlockingQueue<>(100000);

        client = new ClientBuilder()
                .hosts(Constants.STREAM_HOST)
                .authentication(authentication)
                .endpoint(endpoint)
                .processor(new StringDelimitedProcessor(queue))
                .build();
        gson = new Gson();

   }

    private org.apache.kafka.clients.producer.Producer<Long, String> getProducer(String servers) {
        Properties properties = new Properties();
        properties.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, servers);
        properties.put(ProducerConfig.ACKS_CONFIG, "1");
        properties.put(ProducerConfig.LINGER_MS_CONFIG, 500);
        properties.put(ProducerConfig.RETRIES_CONFIG, 0);
        properties.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, LongSerializer.class.getName());
        properties.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

        return new KafkaProducer<>(properties);
    }

    @Override
    public void produce(String brokers, String topicName) throws IOException {
        client.connect();
        try (org.apache.kafka.clients.producer.Producer<Long, String> producer = getProducer(brokers)){
            while (true) {
                Tweet tweet = gson.fromJson(queue.take(), Tweet.class);
                long key = tweet.getId();
                String msg = tweet.toString();
                ProducerRecord<Long, String> record = new ProducerRecord<>(topicName, key, msg);
                producer.send(record, new Callback() {
                    @Override
                    public void onCompletion(RecordMetadata metadata, Exception exception) {
                        if (exception == null) {
                            System.out.printf("Message with offset %d acknowledged by partition %d\n",
                                    metadata.offset(), metadata.partition());
                        } else {
                            System.out.println(exception.getMessage());
                        }
                    }
                });


            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            client.stop();
        }
    }

}
