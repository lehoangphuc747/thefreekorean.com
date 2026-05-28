import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyAbvorAF9gyGlF0FIyahIZfrRyFk9HpL3Q",
  authDomain: "thefreekorean.firebaseapp.com",
  projectId: "thefreekorean",
  storageBucket: "thefreekorean.firebasestorage.app",
  messagingSenderId: "280419896258",
  appId: "1:280419896258:web:99c2daeafb5a9509e4245b",
};

export const app = initializeApp(firebaseConfig);
