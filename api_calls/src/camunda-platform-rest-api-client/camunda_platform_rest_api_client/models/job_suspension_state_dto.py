from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobSuspensionStateDto")


@attr.s(auto_attribs=True)
class JobSuspensionStateDto:
    """ """

    suspended: Union[Unset, None, bool] = UNSET
    job_definition_id: Union[Unset, None, str] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    process_definition_key: Union[Unset, None, str] = UNSET
    process_definition_tenant_id: Union[Unset, None, str] = UNSET
    process_definition_without_tenant_id: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        suspended = self.suspended
        job_definition_id = self.job_definition_id
        process_definition_id = self.process_definition_id
        process_instance_id = self.process_instance_id
        process_definition_key = self.process_definition_key
        process_definition_tenant_id = self.process_definition_tenant_id
        process_definition_without_tenant_id = self.process_definition_without_tenant_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if job_definition_id is not UNSET:
            field_dict["jobDefinitionId	"] = job_definition_id
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if process_definition_key is not UNSET:
            field_dict["processDefinitionKey"] = process_definition_key
        if process_definition_tenant_id is not UNSET:
            field_dict["processDefinitionTenantId"] = process_definition_tenant_id
        if process_definition_without_tenant_id is not UNSET:
            field_dict["processDefinitionWithoutTenantId"] = process_definition_without_tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        suspended = d.pop("suspended", UNSET)

        job_definition_id = d.pop("jobDefinitionId	", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        process_definition_key = d.pop("processDefinitionKey", UNSET)

        process_definition_tenant_id = d.pop("processDefinitionTenantId", UNSET)

        process_definition_without_tenant_id = d.pop("processDefinitionWithoutTenantId", UNSET)

        job_suspension_state_dto = cls(
            suspended=suspended,
            job_definition_id=job_definition_id,
            process_definition_id=process_definition_id,
            process_instance_id=process_instance_id,
            process_definition_key=process_definition_key,
            process_definition_tenant_id=process_definition_tenant_id,
            process_definition_without_tenant_id=process_definition_without_tenant_id,
        )

        job_suspension_state_dto.additional_properties = d
        return job_suspension_state_dto

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
