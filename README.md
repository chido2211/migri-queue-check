# Migri queue check

A simple python script which uses Kamu bot api endpoint to check for your migri
(Finnish Immigration Service) application (Residence permit or Citizenship)
place in their queue

Inspired by: https://github.com/InkMakhova/migri-telegram-bot

# Usage

Supply your application diary number (xxxx/xxx/xxxx) in `diary_nr_1` variable
with `output_dir` then run the script:

```
./main.py
```

You can integrate it with a task scheduler like `cron` to execute daily.
