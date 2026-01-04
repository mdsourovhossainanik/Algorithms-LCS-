"""Shortest Path বের করা —
একটি source node থেকে সব node পর্যন্ত সবচেয়ে কম দূরত্বের পথ (minimum distance path) বের করে।

একটিকে source হিসেবে ধরে তার distance = 0 রাখে।

পাশের nodes গুলোর distance update করে (যদি কম পাওয়া যায়)।

যেই node-এর distance সবচেয়ে কম, তাকে "visited" হিসেবে mark করে।

এইভাবে সব nodes এর জন্য repeat করে

usecase-->Network routing, GPS path finding, data packet delivery optimization।
   this is Greedy approach for Path finding"""
   
#একটি source vertex থেকে অন্য সব vertex পর্যন্ত সবচেয়ে ছোট দূরত্বের পথ বের করা।   