# Internal Messages (`internal-messages`)

Receive internal messages.


## Contents

- [Fields](#fields)




## Fields


| Field | Type | Required | Description |
|---|---|:---:|---|
| `limit` | `number` (`integer`) |  | The number of times to run the input. |
| `filter-kind` | [`Filter Kind`](#filter-kind-options) |  | Specifies whether the message originated from the "system" or by the "user". |
| `filter-source` | [`Filter Source`](#filter-source-options) |  | Specifies what process generated the message.  Was it a "server", "worker" or "job"? |
| `filter-worker` | `string` |  | Specifies what worker to select. |
| `filter-job` | `string` |  | Specifies the name of the job that the message came from. |
| `filter-type` | [`Filter Type`](#filter-type-options) |  | Specifies that particular types of message ought to match. |
| `filter-tag` | `string` |  | Specifies that messages matched ought to carry a tag with a particular value.  This only matches against user-generated messages. |







<h3 id="filter-kind-options">Filter Kind Options</h3>

| Value | Name | Description |
|---|---|---|
| `system` | system | System |
| `user` | user | User |



<h3 id="filter-source-options">Filter Source Options</h3>

| Value | Name | Description |
|---|---|---|
| `job` | job | Job |
| `worker` | worker | Worker |
| `server` | server | Server |



<h3 id="filter-type-options">Filter Type Options</h3>

| Value | Name | Description |
|---|---|---|
| `worker-licensed` | worker-licensed | Worker Licensed |
| `worker-unlicensed` | worker-unlicensed | Worker Unlicensed |
| `all-variables` | all-variables | All Variables |
| `begin-shutting-down-job` | begin-shutting-down-job | Begin Shutting Down Job |
| `begin-shutting-down-server` | begin-shutting-down-server | Begin Shutting Down Server |
| `begin-shutting-down-worker` | begin-shutting-down-worker | Begin Shutting Down Worker |
| `broadcast-job-thread-state` | broadcast-job-thread-state | Broadcast Job Thread State |
| `broadcast-server-thread-state` | broadcast-server-thread-state | Broadcast Server Thread State |
| `broadcast-worker-thread-state` | broadcast-worker-thread-state | Broadcast Worker Thread State |
| `check-job-report-time` | check-job-report-time | Check Job Report Time |
| `check-worker-report-time` | check-worker-report-time | Check Worker Report Time |
| `de-register-job-thread-dependency` | de-register-job-thread-dependency | De Register Job Thread Dependency |
| `de-register-server-thread-dependency` | de-register-server-thread-dependency | De Register Server Thread Dependency |
| `de-register-worker-thread-dependency` | de-register-worker-thread-dependency | De Register Worker Thread Dependency |
| `deployed-job-active` | deployed-job-active | Deployed Job Active |
| `deployed-job-removed` | deployed-job-removed | Deployed Job Removed |
| `deployed-job-should-be-running` | deployed-job-should-be-running | Deployed Job Should Be Running |
| `heart-beat` | heart-beat | Heart Beat |
| `initialise-internal-state` | initialise-internal-state | Initialise Internal State |
| `initialise-job-states` | initialise-job-states | Initialise Job States |
| `job-batch-end` | job-batch-end | Job Batch End |
| `job-deploy-ready` | job-deploy-ready | Job Deploy Ready |
| `job-deployed` | job-deployed | Job Deployed |
| `job-document-end` | job-document-end | Job Document End |
| `job-document-start` | job-document-start | Job Document Start |
| `job-errors` | job-errors | Job Errors |
| `job-finished` | job-finished | Job Finished |
| `job-idle` | job-idle | Job Idle |
| `job-initiated` | job-initiated | Job Initiated |
| `job-is-processing` | job-is-processing | Job Is Processing |
| `job-logs` | job-logs | Job Logs |
| `job-metrics` | job-metrics | Job Metrics |
| `job-removing` | job-removing | Job Removing |
| `job-removed` | job-removed | Job Removed |
| `job-remove-failed` | job-remove-failed | Job Remove Failed |
| `job-remove-ready` | job-remove-ready | Job Remove Ready |
| `job-replaced` | job-replaced | Job Replaced |
| `job-required` | job-required | Job Required |
| `job-run-ended` | job-run-ended | Job Run Ended |
| `job-runtime-error` | job-runtime-error | Job Runtime Error |
| `job-run-started` | job-run-started | Job Run Started |
| `job-running-docker` | job-running-docker | Job Running Docker |
| `job-running-script` | job-running-script | Job Running Script |
| `job-running-subprocess` | job-running-subprocess | Job Running Subprocess |
| `job-running-system-d` | job-running-system-d | Job Running System D |
| `job-settings` | job-settings | Job Settings |
| `job-step-statistics` | job-step-statistics | Job Step Statistics |
| `job-started` | job-started | Job Started |
| `job-staged` | job-staged | Job Staged |
| `job-shutting-down` | job-shutting-down | Job Shutting Down |
| `job-stopping` | job-stopping | Job Stopping |
| `job-stopped` | job-stopped | Job Stopped |
| `job-timed-out` | job-timed-out | Job Timed Out |
| `job-suspicious-silence` | job-suspicious-silence | Job Suspicious Silence |
| `job-thread-state` | job-thread-state | Job Thread State |
| `job-trace` | job-trace | Job Trace |
| `job-trace-requires-samples` | job-trace-requires-samples | Job Trace Requires Samples |
| `job-updated` | job-updated | Job Updated |
| `job-worker-comms-error` | job-worker-comms-error | Job Worker Comms Error |
| `license-state-changed` | license-state-changed | License State Changed |
| `license-validation-failed` | license-validation-failed | License Validation Failed |
| `license-validation-ok` | license-validation-ok | License Validation Ok |
| `license-volume-violation` | license-volume-violation | License Volume Violation |
| `new-license` | new-license | New License |
| `override-job-coordinated-shutdown` | override-job-coordinated-shutdown | Override Job Coordinated Shutdown |
| `override-server-coordinated-shutdown` | override-server-coordinated-shutdown | Override Server Coordinated Shutdown |
| `override-worker-coordinated-shutdown` | override-worker-coordinated-shutdown | Override Worker Coordinated Shutdown |
| `register-job-thread-dependency` | register-job-thread-dependency | Register Job Thread Dependency |
| `register-server-thread-dependency` | register-server-thread-dependency | Register Server Thread Dependency |
| `register-worker-thread-dependency` | register-worker-thread-dependency | Register Worker Thread Dependency |
| `run-job-failure` | run-job-failure | Run Job Failure |
| `server-logs` | server-logs | Server Logs |
| `server-started` | server-started | Server Started |
| `server-starting` | server-starting | Server Starting |
| `server-stopping` | server-stopping | Server Stopping |
| `server-thread-state` | server-thread-state | Server Thread State |
| `server-worker-comms-error` | server-worker-comms-error | Server Worker Comms Error |
| `shutdown-jobs` | shutdown-jobs | Shutdown Jobs |
| `shutdown-worker` | shutdown-worker | Shutdown Worker |
| `system-shutdown` | system-shutdown | System Shutdown |
| `update-upstream-sync-for-job` | update-upstream-sync-for-job | Update Upstream Sync For Job |
| `update-upstream-sync-for-worker` | update-upstream-sync-for-worker | Update Upstream Sync For Worker |
| `update-variable` | update-variable | Update Variable |
| `user-alert` | user-alert | User Alert |
| `user-generated` | user-generated | User Generated |
| `user-notification` | user-notification | User Notification |
| `worker-command-for-job` | worker-command-for-job | Worker Command For Job |
| `worker-connected` | worker-connected | Worker Connected |
| `worker-created` | worker-created | Worker Created |
| `worker-debug-heart-beat` | worker-debug-heart-beat | Worker Debug Heart Beat |
| `worker-error` | worker-error | Worker Error |
| `worker-heart-beat` | worker-heart-beat | Worker Heart Beat |
| `worker-logs` | worker-logs | Worker Logs |
| `worker-offline` | worker-offline | Worker Offline |
| `worker-server-comms-error` | worker-server-comms-error | Worker Server Comms Error |
| `worker-settings` | worker-settings | Worker Settings |
| `worker-shutdown` | worker-shutdown | Worker Shutdown |
| `worker-shutting-down` | worker-shutting-down | Worker Shutting Down |
| `worker-started` | worker-started | Worker Started |
| `worker-state-uuid` | worker-state-uuid | Worker State Uuid |
| `worker-stopping` | worker-stopping | Worker Stopping |
| `worker-suspicious-silence` | worker-suspicious-silence | Worker Suspicious Silence |
| `worker-system-information` | worker-system-information | Worker System Information |
| `worker-thread-state` | worker-thread-state | Worker Thread State |
| `worker-updated` | worker-updated | Worker Updated |
| `worker-modified` | worker-modified | Worker Modified |
| `worker-removed` | worker-removed | Worker Removed |
| `context-changed` | context-changed | Context Changed |
| `rerender-deployment` | rerender-deployment | Rerender Deployment |
| `job-killed` | job-killed | Job Killed |




---
Prev: [HTTP Server](http-server.md)  
Next: [Log Files](files.md)  
