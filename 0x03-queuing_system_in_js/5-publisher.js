import { createClient } from "redis";
import { setTimeout } from "timers/promises";

const client = createClient()

  .on("Error", (err) => { console.log(`Redis client not connected to the server: ${err}`)})

client.connect();

console.log("Redis client connected to the server");

async function publishMessage(message, time) {
  await setTimeout(time);
  console.log(`About to send ${message}`);
  client.publish('ALXchannel', message);
}

publishMessage("ALX Student #1 starts course", 100);
publishMessage("ALX Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("ALX Student #3 starts course", 400);
