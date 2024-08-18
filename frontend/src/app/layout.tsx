import type { Metadata } from "next";
import Link from 'next/link';
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "FryDay",
  description: "Ravintola FryDay",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <title>FryDay</title>
      </head>
      <body>
        <header className="flex justify-between items-center p-4 bg-orange-600">
          <div className="logo">
            <img src="/images/logo.png" alt="FryDay Logo" className="w-12 h-12" />
          </div>
          <nav className="flex space-x-4">
            <Link href="/chicken">Chicken</Link>
            <Link href="/about">About Us</Link>
            <Link href="/cafe">Our Cafe</Link>
            <Link href="/location">Location</Link>
          </nav>
          <div className="cart">
            <img src="/images/cart.png" alt="Cart" className="w-6 h-6" />
          </div>
        </header>
        <main>{children}</main>
      </body>
    </html>
  );
}
