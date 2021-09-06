from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchDto")


@attr.s(auto_attribs=True)
class BatchDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    total_jobs: Union[Unset, None, int] = UNSET
    jobs_created: Union[Unset, None, int] = UNSET
    batch_jobs_per_seed: Union[Unset, None, int] = UNSET
    invocations_per_batch_job: Union[Unset, None, int] = UNSET
    seed_job_definition_id: Union[Unset, None, str] = UNSET
    monitor_job_definition_id: Union[Unset, None, str] = UNSET
    batch_job_definition_id: Union[Unset, None, str] = UNSET
    suspended: Union[Unset, None, bool] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    create_user_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        total_jobs = self.total_jobs
        jobs_created = self.jobs_created
        batch_jobs_per_seed = self.batch_jobs_per_seed
        invocations_per_batch_job = self.invocations_per_batch_job
        seed_job_definition_id = self.seed_job_definition_id
        monitor_job_definition_id = self.monitor_job_definition_id
        batch_job_definition_id = self.batch_job_definition_id
        suspended = self.suspended
        tenant_id = self.tenant_id
        create_user_id = self.create_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if total_jobs is not UNSET:
            field_dict["totalJobs"] = total_jobs
        if jobs_created is not UNSET:
            field_dict["jobsCreated"] = jobs_created
        if batch_jobs_per_seed is not UNSET:
            field_dict["batchJobsPerSeed"] = batch_jobs_per_seed
        if invocations_per_batch_job is not UNSET:
            field_dict["invocationsPerBatchJob"] = invocations_per_batch_job
        if seed_job_definition_id is not UNSET:
            field_dict["seedJobDefinitionId"] = seed_job_definition_id
        if monitor_job_definition_id is not UNSET:
            field_dict["monitorJobDefinitionId"] = monitor_job_definition_id
        if batch_job_definition_id is not UNSET:
            field_dict["batchJobDefinitionId"] = batch_job_definition_id
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if create_user_id is not UNSET:
            field_dict["createUserId"] = create_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        total_jobs = d.pop("totalJobs", UNSET)

        jobs_created = d.pop("jobsCreated", UNSET)

        batch_jobs_per_seed = d.pop("batchJobsPerSeed", UNSET)

        invocations_per_batch_job = d.pop("invocationsPerBatchJob", UNSET)

        seed_job_definition_id = d.pop("seedJobDefinitionId", UNSET)

        monitor_job_definition_id = d.pop("monitorJobDefinitionId", UNSET)

        batch_job_definition_id = d.pop("batchJobDefinitionId", UNSET)

        suspended = d.pop("suspended", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        create_user_id = d.pop("createUserId", UNSET)

        batch_dto = cls(
            id=id,
            type=type,
            total_jobs=total_jobs,
            jobs_created=jobs_created,
            batch_jobs_per_seed=batch_jobs_per_seed,
            invocations_per_batch_job=invocations_per_batch_job,
            seed_job_definition_id=seed_job_definition_id,
            monitor_job_definition_id=monitor_job_definition_id,
            batch_job_definition_id=batch_job_definition_id,
            suspended=suspended,
            tenant_id=tenant_id,
            create_user_id=create_user_id,
        )

        batch_dto.additional_properties = d
        return batch_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
