# Flowchart — Examination Result

```text
  +-------+
  | START |
  +---+---+
      |
      v
+----------------------+
| Input five marks     |
+----------+-----------+
           |
           v
+----------------------+
| Are all marks 0-100? |
+------+----------+----+
       | Yes      | No
       v          v
+----------------+  +----------------+
| Find failed    |  | Display invalid|
| subjects       |  | marks message  |
+-------+--------+  +-------+--------+
        |                   |
        v                   v
+----------------------+  +-----+
| Apply eligible grace |  | END |
| mark if allowed      |  +-----+
+----------+-----------+
           |
           v
+----------------------+
| Calculate total and  |
| percentage          |
+----------+-----------+
           |
           v
+----------------------+
| All subjects passed? |
+------+----------+----+
       | Yes      | No
       v          v
+-----------+  +-----------+
| Show PASS |  | Show FAIL |
+-----+-----+  +-----+-----+
      |              |
      +------+-------+
             v
          +-----+
          | END |
          +-----+
```