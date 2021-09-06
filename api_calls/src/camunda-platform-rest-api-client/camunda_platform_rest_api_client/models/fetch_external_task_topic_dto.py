from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr

from ..models.fetch_external_task_topic_dto_process_variables import FetchExternalTaskTopicDtoProcessVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="FetchExternalTaskTopicDto")


@attr.s(auto_attribs=True)
class FetchExternalTaskTopicDto:
    """ """

    topic_name: str
    lock_duration: Optional[int]
    variables: Union[Unset, None, List[str]] = UNSET
    local_variables: Union[Unset, None, bool] = False
    business_key: Union[Unset, None, str] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_definition_id_in: Union[Unset, None, List[str]] = UNSET
    process_definition_key: Union[Unset, None, str] = UNSET
    process_definition_key_in: Union[Unset, None, List[str]] = UNSET
    process_definition_version_tag: Union[Unset, None, str] = UNSET
    without_tenant_id: Union[Unset, None, bool] = False
    tenant_id_in: Union[Unset, None, List[str]] = UNSET
    process_variables: Union[Unset, FetchExternalTaskTopicDtoProcessVariables] = UNSET
    deserialize_values: Union[Unset, None, bool] = False
    include_extension_properties: Union[Unset, None, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        topic_name = self.topic_name
        lock_duration = self.lock_duration
        variables: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.variables, Unset):
            if self.variables is None:
                variables = None
            else:
                variables = self.variables

        local_variables = self.local_variables
        business_key = self.business_key
        process_definition_id = self.process_definition_id
        process_definition_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.process_definition_id_in, Unset):
            if self.process_definition_id_in is None:
                process_definition_id_in = None
            else:
                process_definition_id_in = self.process_definition_id_in

        process_definition_key = self.process_definition_key
        process_definition_key_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.process_definition_key_in, Unset):
            if self.process_definition_key_in is None:
                process_definition_key_in = None
            else:
                process_definition_key_in = self.process_definition_key_in

        process_definition_version_tag = self.process_definition_version_tag
        without_tenant_id = self.without_tenant_id
        tenant_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tenant_id_in, Unset):
            if self.tenant_id_in is None:
                tenant_id_in = None
            else:
                tenant_id_in = self.tenant_id_in

        process_variables: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.process_variables, Unset):
            process_variables = self.process_variables.to_dict()

        deserialize_values = self.deserialize_values
        include_extension_properties = self.include_extension_properties

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topicName": topic_name,
                "lockDuration": lock_duration,
            }
        )
        if variables is not UNSET:
            field_dict["variables"] = variables
        if local_variables is not UNSET:
            field_dict["localVariables"] = local_variables
        if business_key is not UNSET:
            field_dict["businessKey"] = business_key
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_definition_id_in is not UNSET:
            field_dict["processDefinitionIdIn"] = process_definition_id_in
        if process_definition_key is not UNSET:
            field_dict["processDefinitionKey"] = process_definition_key
        if process_definition_key_in is not UNSET:
            field_dict["processDefinitionKeyIn"] = process_definition_key_in
        if process_definition_version_tag is not UNSET:
            field_dict["processDefinitionVersionTag"] = process_definition_version_tag
        if without_tenant_id is not UNSET:
            field_dict["withoutTenantId"] = without_tenant_id
        if tenant_id_in is not UNSET:
            field_dict["tenantIdIn"] = tenant_id_in
        if process_variables is not UNSET:
            field_dict["processVariables"] = process_variables
        if deserialize_values is not UNSET:
            field_dict["deserializeValues"] = deserialize_values
        if include_extension_properties is not UNSET:
            field_dict["includeExtensionProperties"] = include_extension_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        topic_name = d.pop("topicName")

        lock_duration = d.pop("lockDuration")

        variables = cast(List[str], d.pop("variables", UNSET))

        local_variables = d.pop("localVariables", UNSET)

        business_key = d.pop("businessKey", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_definition_id_in = cast(List[str], d.pop("processDefinitionIdIn", UNSET))

        process_definition_key = d.pop("processDefinitionKey", UNSET)

        process_definition_key_in = cast(List[str], d.pop("processDefinitionKeyIn", UNSET))

        process_definition_version_tag = d.pop("processDefinitionVersionTag", UNSET)

        without_tenant_id = d.pop("withoutTenantId", UNSET)

        tenant_id_in = cast(List[str], d.pop("tenantIdIn", UNSET))

        _process_variables = d.pop("processVariables", UNSET)
        process_variables: Union[Unset, FetchExternalTaskTopicDtoProcessVariables]
        if isinstance(_process_variables, Unset):
            process_variables = UNSET
        else:
            process_variables = FetchExternalTaskTopicDtoProcessVariables.from_dict(_process_variables)

        deserialize_values = d.pop("deserializeValues", UNSET)

        include_extension_properties = d.pop("includeExtensionProperties", UNSET)

        fetch_external_task_topic_dto = cls(
            topic_name=topic_name,
            lock_duration=lock_duration,
            variables=variables,
            local_variables=local_variables,
            business_key=business_key,
            process_definition_id=process_definition_id,
            process_definition_id_in=process_definition_id_in,
            process_definition_key=process_definition_key,
            process_definition_key_in=process_definition_key_in,
            process_definition_version_tag=process_definition_version_tag,
            without_tenant_id=without_tenant_id,
            tenant_id_in=tenant_id_in,
            process_variables=process_variables,
            deserialize_values=deserialize_values,
            include_extension_properties=include_extension_properties,
        )

        fetch_external_task_topic_dto.additional_properties = d
        return fetch_external_task_topic_dto

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
