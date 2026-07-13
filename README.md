# py_code_library-
Tested and documented code

## Structure

Each task lives in its own folder, with a matching short entry in `the_code_info/`
so existing tasks can be found before anything gets rebuilt.

```
py_code_library-/
├── the_code_info/
│   ├── index.md                     one line per task, searched first
│   └── <task_name>.md               full doc for one task
│
├── task_<task_name>/
│   ├── .env.example
│   ├── requirements.txt
│   ├── <task_name>.py
│   └── <task_name>_test.ipynb
│
└── pipeline_<name>/                 same shape, for chained multi-step work
```

Before building anything new, check `the_code_info/index.md` first.
