import express, { Request, Response } from 'express';
import mongoose from 'mongoose';
import redis from 'redis';
import bodyParser from 'body-parser';

const app = express();
const PORT: number = 3000;

// Connect to MongoDB
const MONGO_HOST: string = process.env.MONGO_HOST || 'localhost';
const MONGO_PORT: number = Number(process.env.MONGO_PORT) || 27017;

mongoose.connect(`mongodb://${MONGO_HOST}:${MONGO_PORT}/mydb`, {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// Connect to Redis
const REDIS_HOST: string = process.env.REDIS_HOST || 'localhost';
const REDIS_PORT: number = Number(process.env.REDIS_PORT) || 6379;

const redisClient = redis.createClient({
    host: REDIS_HOST,
    port: REDIS_PORT
});
redisClient.on('error', err => {
    console.log('Redis error: ', err);
});

// MongoDB Model
interface MyModelInterface extends mongoose.Document {
    name: string;
}

const MySchema = new mongoose.Schema({
    name: String
});

const MyModel = mongoose.model<MyModelInterface>('MyModel', MySchema);

app.use(bodyParser.json());

app.get('/names', async (req: Request, res: Response) => {
    try {
        const documents = await MyModel.find({});
        const names = documents.map(doc => doc.name);
        res.json(names);
    } catch (err) {
        res.status(500).send(err.message);
    }
});

app.post('/set-redis', (req: Request, res: Response) => {
    const { key, value } = req.body;
    
    if (!key || !value) {
        return res.status(400).send('Both key and value are required');
    }

    redisClient.set(key, value, (err) => {
        if (err) return res.status(500).send(err.message);
        res.status(200).send('Value set successfully in Redis');
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
