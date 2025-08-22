import { createClient } from "redis";

const client = createClient()
  .on("Error", (err) => console.log(`Redis client not connected to the server: ${err}`));

await client.connect();

console.log("Redis client connected to the server")

const listener = (message, channel) => {
  console.log(message)
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
  }
};

client.subscribe('ALXchannel', listener);
