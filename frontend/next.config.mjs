/** @type {import('next').NextConfig} */
import { join } from 'path';
import { config } from 'dotenv';

// Load environment variables from .env file
config({ path: join(process.cwd(), '.env') });

const nextConfig = {
  env: {
    API_URL: process.env.API_URL,
  },
};

export default nextConfig;