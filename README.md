# ChaabiAssignPromit


Dataset used from BigBasket.

![image](https://github.com/PromitHal/ChaabiAssignPromit/assets/83832850/f22c5970-20b1-4a1f-905d-7034d1ab964a)

**Initial Steps**
1. Ensure docker is installed.
   
**Install these libraries**
# !pip install qdrant-client --user
# !pip install faker
# !pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# !pip install sentence_transformers
# !pip install fastapi uvicorn


2. Go to data_loader.py
    // replace these as per your needs
    collection_name="Promit_BIGBasket_CHAABI"
    path_data=r'bigb.csv'
    name_model="all-MiniLM-L6-v2"
    device="cuda"
  A json file corresponding to the data would be saved as "file.json".
  A numpy file corresponding to embedded vectors would be saved as "vectors.npy"
  Vector database would be created and data would be uploaded.
  Ensure Docker is running in backgroumd.
3. You are almost ready to go!
   Go to the terminal and enter " python main.py".
   Hurray! now move to: http://localhost:8085/docs#/default/search_startup_api_search_get
   Click on "GET".
   Click on "Try it"
   Enter your query!
   See and enjoy the results.
   
Modules:
1. Main.py
2. NeuralSearch.py
3. MMR.py
4. data_loader.py

   **Main.py**: Used for deploying the app using Fast API
   Please mention collection name in the "collection_name" variable in main.py

   **NeuralSearch.py**:
   Please enter your OPEN_AI api key.
   Implements search from the vector database corresponding to "collection_name".
   Cosine similarity based search.
   Intially, 20 most similar vectors are retrieved.
   Maximum Margin Relevance Algorithm (MMR) is used to re-rank the results to ensure diversity, and top 5 results are selected.
   Call to GPT-3.5 Turbo (CHAT GPT) is made with prompt like this:![image](https://github.com/PromitHal/ChaabiAssignPromit/assets/83832850/a3fa043d-fdf8-4fd4-9da5-6d1f379c6577)
   Summarized results are returned.

   **MMR.py**
   Implementation of MMR algorithm from scratch.
   Lambda parameter is kept at 0.5, can be changed accordingly.



# User query: "Paneer items"
![image](https://github.com/PromitHal/ChaabiAssignPromit/assets/83832850/33410855-4f3f-4134-864e-c09d3425f5c2)


**User query: "Some snacks"**
Introducing some exciting snacks for your taste buds! First up, we have Tong Garden's Party Snack consisting of peanuts, green peas, broad beans, and chickpeas with a delicious combination of soybean, garlic, sesame seed, chili, and pepper. This trail and cocktail mix is a hit among guests with a high rating of 4.5. It is available at a discounted price of $255 from its original market price of $300. Another option from Tong Garden is their Party Snack in a variety pack at a sale price of $148.75, down from $175. This snack is perfect for gatherings and has a rating of 4.4. Next up, we have GoodDiet's Multigrain Balls - Chilli Chataka, a healthy and baked snacking option made from a unique mix of corn, jowar, and rice with a spicy masala flavor. It is available for just $70. Looking for a fun snacking solution? Check out the Disney Mickey Mouse 2 in 1 Snackeez Bottle with Snack Box from Hm International. This innovative snack container keeps your drink and favorite snack in one hand, with a spill-proof seal and cute cartoon character design. It is available at a discounted price of $269 from its market price of $299. Lastly, we have Parle's Wafers - Aloo Chaat, an authentic and flavorful snack made from the finest ingredients. This delightful treat is perfect for parties and get-togethers, and it is priced at only $20.1, down from $30. With such a wide range of snacks to choose from, these options will surely satisfy your snacking needs!


**User query: "Beauty and care products"**

We found 5 beauty and care products that match your search query. \n\n1. The Face Wash - Acne Clear by Dr.Batra'S is a popular choice among customers, with a rating of 3.4. It moisturizes and tightens the skin, preventing wrinkles and fighting acne. The market price is $115, but it is currently on sale for $63.25.\n\n2. Another product by Dr.Batra'S is the Natural Moisturising Lotion, Enriched with Echinacea & Aloevera. It helps with cellular regeneration and is suitable for face care. However, it has a lower rating of just 1.0. The market price is $199, but it is currently available for $99.5.\n\n3. We also have the Flawless Papaya Face Pack by Natures Essence. This product is specially formulated to brighten the skin tone and reduce discoloration. It has a high rating of 4.1 and is priced at $75.\n\n4. For men's grooming, we have the Eau De Cologne - Regular by Premium. It is an anti-bacterial agent and keeps bacterial infections away. Customers seem to love its unique fragrance, as it has a rating of 4.4. The market price is $135.\n\nThese are just a few of the options available. For more beauty tips and tricks, you can visit our blog at https://bigbasket.blog/.



**User query: "Winter creams"**

Our search for winter creams on the database returned a total of 5 results. The first result is the \"Berries n Cream\" ice cream stick by London Dairy, priced at Rs. 135. It is described as a connoisseur's delight with a combination of flavors including fresh cream cheese, berry blend, and a coating of yogurt flavor with crunchy biscuit. The second result is the \"Cold Cream + Honey & Milk Protein\" by Ponds, priced at Rs. 134.4. It is highly rated at 4.2 stars and is promoted as a moisturizing cream that prevents dry skin during the winter season. The third result is the \"Black Currant\" ice cream by Baskin Robbins, available at a discount price of Rs. 328.5. It is described as a creamy and delicious ice cream with black currant pieces and raisins. The fourth result is the \"Cafe Mocha\" ice cream by THE BROOKLYN CREAMERY, currently on sale for Rs. 206.25. It is a low-calorie coffee-flavored ice cream with a chocolate swirl, made with 100% cane sugar. The fifth and final result is \"Heritage Fresh Cream,\" priced at Rs. 47, which is described as smooth and versatile for both sweet and savory dishes. Overall, these winter creams offer a range of flavors and moisturizing benefits to cater to different preferences and skincare needs."


**User query: "Fruits"**
We found 5 results for your search query on fruits. \n\n1. Rasna Fruit Juice - Fruit Plus, Florida Orange: This product is a fruit powder mix, fortified with 21 vitamins and minerals. It can be made in just 5 seconds without the need to add sugar. Each pack makes 39 glasses (180ml each) and captures the delightful taste of freshly squeezed oranges. The market price is ₹240.0, but it is currently on sale for ₹210.0. It has a rating of 3.8 out of 5. bb Royal Mixed Dry Fruits: This pack contains a mix of almonds, raisins, figs, plain pista, and cashews. These dry fruits are considered rich suppliers of nutrients and can be consumed raw or used in various food items to add flavor. The market price is ₹750.0, but it is currently on sale for ₹522.0. The rating for this product is not available. Fresho Signature Assorted Just Berries, Fruits, Nuts, and Seeds pack: This pack contains a mix of berries, fruits, nuts, and seeds. It is good for the eyes, heart, skin, bones, liver, and boosts immunity. It also improves digestion, prevents aging, and is rich in antioxidants. The market price is ₹365.0, but it is currently on sale for ₹229.0. The rating for this product is not available. Tropicana Fruit Juice - Delight, Orange: Enjoy the refreshing taste of oranges with this ready-to-serve fruit beverage from Tropicana. It is protected with a special 6-layer packaging to retain its taste and goodness. Oranges are also known as Tangerines and Mandarins and are a great refresher. The market price for this juice is ₹600.0, and it has a rating not available.\n\n5. Tong Garden Nuts & Dried Berry Mix: This snack consists of a medley of nuts and dried fruits, including macadamia, walnuts, almonds, cashews, pumpkin seeds, dried blueberries, cranberries, and jumbo Thompson raisins. It is high in antioxidants, protein, and fiber, providing delicious and healthy snacking options. The market price is ₹250.0, but it is currently on sale for ₹212.5. The rating for this product is not available.\n\nThese products offer a variety of fruit-related options, including fruit juices, dry fruits, and healthy snack mixes. Hurry up and take advantage of the ongoing sale prices!

**User query: "Milk Products"**
We found a variety of milk products based on your search query. The first result is the Rica Milk Wax, a beauty and hygiene product. It contains milk proteins, vitamins, and minerals to provide nourishment and hydration to the skin. With a rating of 4.0, it is suitable for sensitive skin and offers superior hair grip during waxing. The market price for this product is 990.0.\n\nNext, we have Nestle A+ Nourish Toned Milk, which falls under the bakery, cakes, and dairy category. Produced from the purest milk, it undergoes hygienic industrial processes. This toned milk can be consumed twice a day and is available in a 1-liter carton. The market price for this product is 1020.0, but currently on sale for 768.48.\n\nAnother option is MilkLane's UHT Processed Homogenized Toned Milk, which is also from the bakery, cakes, and dairy category. It has a lower fat content than normal milk and is rich in calcium, protein, and vitamin D. This milk strengthens bones, teeth, and muscles, and is priced at 140.0.\n\nNestle Cream - Original is a dairy product falling under the gourmet and world food category. It is light, fluffy, and perfect for adding to coffee or fruit salads to enhance their flavor and consistency. This pure dairy sterilized cream is produced in Holland and Brazil. The market price for this product is 350.0, but currently on sale for 262.5.\n\nLastly, Amul Slim 'n' Trim Skimmed Milk is a pasteurized milk product that meets PFA standards. It is considered the most hygienic liquid milk available in the market. Packaged in pouches for convenience, this milk is priced at 150.0 and has a high rating of 4.2.\n\nThese milk products offer a range of options to meet different needs, from skincare to dietary preferences.



