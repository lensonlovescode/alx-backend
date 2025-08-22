import { createClient } from "redis";
import pkg from "redis";
const print = pkg;

const client = await createClient();

client.on("error", (err) => console.log(`Redis client not connected to the server: ${err}`));

await client.connect();
console.log("Redis client connected to the server");


async function setNewSchool(schoolName, value) {
  await client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  console.log(await client.get(schoolName));
}


await displaySchoolValue('ALX');
await setNewSchool('ALXSanFransisco', '100');
await displaySchoolValue('ALXSanFransisco');

client.destroy();
