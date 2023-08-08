# wilo

Wilo is a utility for logging in Bash scripts.

Nowadays, all logs are from all systems are collected and forwarded to a centralized location.
For Bash scripts, it always require custom code to generate formatted logs in text or JSON.

__Wilo__ offers a very simple command line interface which will provide formatted logging out-of-the-box.
It is written in Bash and has a single dependency: `jq`.

## Installation

```bash
$ curl -fsSL https://github.com/julbme/wilo/releases/download/v1.0.1/wilo-1.0.1.tar.gz \
    | tar xvzf - -C /tmp
$ sudo mv /tmp/wilo-1.0.1/bin/wilo /usr/local/bin/
$ wilo --version
```

## How to use

### Text logging

The following commands:

```bash
$ wilo trace "A simple message in TRACE"
$ wilo debug "A simple message in DEBUG"
$ wilo info "A simple message in INFO"
$ wilo warn "A simple message in WARN"
$ wilo error "A simple message in ERROR"

# with context
$ export WILO_GLOBAL_CONTEXT="app=some-app,version=1.0.0"
$ wilo info "A simple message with global context"
$ wilo info "A simple message with global and cmd context" --context="step=3"
```

will output the following:

```
2023-08-08T19:32:32.603211+00:00 TRACE [] - A simple message in TRACE
2023-08-08T19:32:32.671374+00:00 DEBUG [] - A simple message in DEBUG
2023-08-08T19:32:32.697156+00:00 INFO [] - A simple message in INFO
2023-08-08T19:32:32.719109+00:00 WARN [] - A simple message in WARN
2023-08-08T19:32:32.739548+00:00 ERROR [] - A simple message in ERROR
2023-08-08T20:01:59.782761+00:00 INFO [app=some-app version=1.0.0] - A simple message with global context
2023-08-08T20:02:04.840306+00:00 INFO [app=some-app version=1.0.0 step=3] - A simple message with global and cmd context
```

### JSON logging

The following commands:

```bash
$ export WILO_OUTPUT_TYPE=json
$ wilo trace "A simple message in TRACE"
$ wilo debug "A simple message in DEBUG"
$ wilo info "A simple message in INFO"
$ wilo warn "A simple message in WARN"
$ wilo error "A simple message in ERROR"

# with context
$ export WILO_GLOBAL_CONTEXT="app=some-app,version=1.0.0"
$ wilo info "A simple message with global context"
$ wilo info "A simple message with global and cmd context" --context="step=3"
```

will output the following:

```
{"time":"2023-08-08T19:33:42.711025+00:00","level":"TRACE","message":"A simple message in TRACE"}
{"time":"2023-08-08T19:33:42.744632+00:00","level":"DEBUG","message":"A simple message in DEBUG"}
{"time":"2023-08-08T19:33:42.768501+00:00","level":"INFO","message":"A simple message in INFO"}
{"time":"2023-08-08T19:33:42.789105+00:00","level":"WARN","message":"A simple message in WARN"}
{"time":"2023-08-08T19:33:42.808758+00:00","level":"ERROR","message":"A simple message in ERROR"}
{"time":"2023-08-08T20:01:02.714245+00:00","level":"INFO","message":"A simple message with global context","app":"some-app","version":"1.0.0"}
{"time":"2023-08-08T20:01:10.452720+00:00","level":"INFO","message":"A simple message with global and cmd context","app":"some-app","version":"1.0.0","step":"3"}
```

## Advanced configuration

|     Environment var     |                               Description                                |   Default    |
|-------------------------|--------------------------------------------------------------------------|--------------|
| `WILO_OUTPUT_TYPE`      | Format of the log: `text`, `textcolor`, `json`.                          | `text`       |
| `WILO_DATE_TIME_FORMAT` | Date/time format: `iso8601utc`, `iso8601`, `ts`, `ts_milli`, `ts_micro`. | `iso8601utc` |
| `WILO_GLOBAL_CONTEXT`   | Context to add to all the logs: `key1=value1,key2=value2`.               | ``           |

