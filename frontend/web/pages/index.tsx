import React from 'react';
import Head from 'next/head';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 to-purple-900">
      <Head>
        <title>FiBace - Управление недвижимостью</title>
      </Head>
      
      <main className="container mx-auto px-4 py-16 text-center">
        <h1 className="text-6xl font-bold text-white mb-4">FiBace 🏢</h1>
        <p className="text-2xl text-gray-300 mb-8">
          Умное управление арендной недвижимостью
        </p>
        <button className="bg-blue-600 text-white px-8 py-3 rounded-lg text-xl hover:bg-blue-700">
          Начать работу
        </button>
      </main>
    </div>
  );
}
