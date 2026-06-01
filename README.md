This project contains solutions for:

1. Django Signals - Synchronous vs Asynchronous behavior
2. Django Signals - Thread behavior
3. Django Signals - Database transaction behavior
4. Iterable Rectangle class in Python





# Accuknox Django Trainee Assignment

## Candidate

Sahil Singh

---

# Question 1: Are Django Signals Synchronous or Asynchronous?

## Experiment

A `post_save` signal handler was created with a deliberate 5-second delay using `time.sleep(5)`.

### Signal

```python
@receiver(post_save, sender=Demo)
def test_signal(sender, instance, **kwargs):
    print("Signal Started")
    time.sleep(5)
    print("Signal Finished")
```

### View

```python
def create_demo(request):
    print("Before Save")

    Demo.objects.create(name="Sahil")

    print("After Save")

    return HttpResponse("Done")
```

### Observed Output

```
Before Save
Signal Started
Signal Finished
After Save
```
Terminal 

<img width="369" height="150" alt="Screenshot from 2026-06-01 13-03-34" src="https://github.com/user-attachments/assets/dc6137f7-3948-40ca-ad39-35acfa59baa7" />



### Conclusion

Since execution after `Demo.objects.create()` did not continue until the signal handler completed, Django signals execute synchronously by default.

---

# Question 2: Do Django Signals Run in the Same Thread as the Caller?

## Experiment

Thread IDs were printed from both the view and the signal handler using `threading.get_ident()`.

### Observed Output

```
View Thread ID: 130868170364608
Signal Thread ID: 130868170364608
```

### Conclusion

The identical thread IDs prove that Django signals execute in the same thread as the caller by default.

---

# Question 3: Do Django Signals Run in the Same Database Transaction as the Caller?

## Experiment

A signal created a `TransactionLog` record whenever a `TransactionDemo` object was saved. The save operation was wrapped inside `transaction.atomic()`, and an exception was intentionally raised to force a rollback.

### Observed Output

```
Transaction Signal Fired
TransactionLog Created
Rollback Happened
TransactionDemo Count: 0
TransactionLog Count: 0
```

### Conclusion

Both records were rolled back together, proving that Django signals participate in the same database transaction as the caller by default.

---

# Rectangle Class

## Requirement

Create an iterable Rectangle class that yields:

```python
{'length': value}
{'width': value}
```

### Example

```python
rect = Rectangle(10, 5)

for item in rect:
    print(item)
```

### Output

```python
{'length': 10}
{'width': 5}
```

---

# Setup Instructions

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```
