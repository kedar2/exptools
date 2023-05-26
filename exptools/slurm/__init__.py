import submitit
from pathlib import Path
from typing import Any, List, Optional, Type, Union

class AutoExecutor(submitit.AutoExecutor):
    """
    AutoExecutor class inheriting from submitit.AutoExecutor with custom settings
    for the MPI cluster.
    """
    def __init__(self,
                 folder: Union[str, Path]="submitit_logs",
                 slurm_job_name: str="myjob",
                 slurm_constraint: str="gpu",
                 slurm_gres: str="gpu:a100:1",
                 slurm_nodes=1,
                 slurm_time="00:30:00",
                 slurm_mem="8G", 
                 **kwargs: Any) -> None:
        # TODO: Add email functionality
        super().__init__(folder=folder, **kwargs)
        self.update_parameters(**kwargs)