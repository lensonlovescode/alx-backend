import { createClient } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log('Redis client not connected to the server: ' + error.toString());
});

await client.connect();

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (_error, reply) => {
    console.log("reply");
  });
};

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
