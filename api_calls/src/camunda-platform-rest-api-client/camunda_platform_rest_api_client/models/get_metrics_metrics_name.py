from enum import Enum


class GetMetricsMetricsName(str, Enum):
    ACTIVITY_INSTANCE_START = "activity-instance-start"
    ACTIVITY_INSTANCE_END = "activity-instance-end"
    JOB_ACQUISITION_ATTEMPT = "job-acquisition-attempt"
    JOB_ACQUIRED_SUCCESS = "job-acquired-success"
    JOB_ACQUIRED_FAILURE = "job-acquired-failure"
    JOB_EXECUTION_REJECTED = "job-execution-rejected"
    JOB_SUCCESSFUL = "job-successful"
    JOB_FAILED = "job-failed"
    JOB_LOCKED_EXCLUSIVE = "job-locked-exclusive"
    EXECUTED_DECISION_ELEMENTS = "executed-decision-elements"
    HISTORY_CLEANUP_REMOVED_PROCESS_INSTANCES = "history-cleanup-removed-process-instances"
    HISTORY_CLEANUP_REMOVED_CASE_INSTANCES = "history-cleanup-removed-case-instances"
    HISTORY_CLEANUP_REMOVED_DECISION_INSTANCES = "history-cleanup-removed-decision-instances"
    HISTORY_CLEANUP_REMOVED_BATCH_OPERATIONS = "history-cleanup-removed-batch-operations"
    HISTORY_CLEANUP_REMOVED_TASK_METRICS = "history-cleanup-removed-task-metrics"
    UNIQUE_TASK_WORKERS = "unique-task-workers"

    def __str__(self) -> str:
        return str(self.value)
