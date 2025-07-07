### Simple To-Do

A simple to-do list application
Here's a sample `README.md` file tailored to your Frappe app (e.g., a simple to-do app), including what you learned, how to run the app, and the challenge you faced:

---

````markdown
# Simple ToDo App - Frappe

## 📘 What I Learned

Through this project, I gained hands-on experience with:

- The Frappe framework and its app development workflow
- Creating custom apps and installing them into a site
- Building DocTypes and using the Web Form feature to interact with users
- Understanding the folder structure and Python-JavaScript integration in Frappe
- Managing the bench CLI for app/site creation, migration, and development
- Setting up routes and working with templates in the Frappe ecosystem

This project helped solidify my understanding of full-stack development using Python-based frameworks.

---

## 🚀 How to Run the App

1. **Navigate to your bench folder**:
   ```bash
   cd /path/to/frappe-bench
````

2. **Start bench**:

   ```bash
   bench start
   ```

3. **Open your browser and go to**:

   ```
   http://localhost:8000
   ```

4. **Log in** using your admin credentials.

5. **Create tasks** using the app’s interface or through the Doctype UI in the Frappe Desk.

> Make sure your custom app is installed on the site and you’ve run `bench migrate` after changes.

---

##  Challenges Faced

One major challenge was **displaying the tasks on a webpage**. Even though the data existed in the database, rendering it dynamically required configuring routes, using the correct Jinja templates, and understanding how Frappe exposes context to web templates.

I had to learn:

* How to create custom pages with `.html` and `.py` files inside the `www` folder
* How to use Jinja templating to loop through tasks
* How to fetch data from a DocType using Frappe's server-side Python methods

Eventually, I managed to resolve it by linking a custom Python script to the route and passing the tasks to the Jinja template properly.

---

## ✅ Final Thoughts

This project gave me a solid foundation in Frappe, and solving real problems (like dynamic task display) made the learning process meaningful. I now feel more confident developing full-fledged apps in Frappe.


### Todo Screenshots

![image](https://github.com/user-attachments/assets/b7549319-7ae2-41b4-954a-8c14aa6d736a)

Create a Task
![image](https://github.com/user-attachments/assets/d41ac5f6-6783-4017-8599-4217f5de21cd)

List Tasks
![image](https://github.com/user-attachments/assets/63b29520-c5f5-4707-8c6e-106ac0881c6e)

Updating a task

![image](https://github.com/user-attachments/assets/8e02a387-e9a7-42ab-b0c4-7489fde10718)

Task Auto hided after completion
![image](https://github.com/user-attachments/assets/b140ae40-7b1a-456d-becd-e6ff8af648d0)


![image](https://github.com/user-attachments/assets/68d475c4-9ba1-4584-bfb7-c086ac98ea55)




