import { createClient } from "redis";
import pkg from "redis";
const { print } = pkg;

const client = createClient()
  .on("Error", (Error) => {
    console.log("Client Error");
  })

console.log("Client connected successfully")

await client.connect();

await client.del("ALX");

await client.hSet("ALX", { Portland: "50", Bogota: "20", Seattle: '80', 'New York': '20', Bogota: '20', Cali: '40', Paris: '2'});

console.log(await client.hGetAll("ALX", print));

await client.destroy();
