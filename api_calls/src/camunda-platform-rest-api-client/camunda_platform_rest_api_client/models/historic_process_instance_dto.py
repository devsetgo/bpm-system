import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.historic_process_instance_dto_state import HistoricProcessInstanceDtoState
from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoricProcessInstanceDto")


@attr.s(auto_attribs=True)
class HistoricProcessInstanceDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    root_process_instance_id: Union[Unset, None, str] = UNSET
    super_process_instance_id: Union[Unset, None, str] = UNSET
    super_case_instance_id: Union[Unset, None, str] = UNSET
    case_instance_id: Union[Unset, None, str] = UNSET
    process_definition_name: Union[Unset, None, str] = UNSET
    process_definition_key: Union[Unset, None, str] = UNSET
    process_definition_version: Union[Unset, None, int] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    business_key: Union[Unset, None, str] = UNSET
    start_time: Union[Unset, None, datetime.datetime] = UNSET
    end_time: Union[Unset, None, datetime.datetime] = UNSET
    removal_time: Union[Unset, None, datetime.datetime] = UNSET
    duration_in_millis: Union[Unset, None, int] = UNSET
    start_user_id: Union[Unset, None, str] = UNSET
    start_activity_id: Union[Unset, None, str] = UNSET
    delete_reason: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    state: Union[Unset, None, HistoricProcessInstanceDtoState] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        root_process_instance_id = self.root_process_instance_id
        super_process_instance_id = self.super_process_instance_id
        super_case_instance_id = self.super_case_instance_id
        case_instance_id = self.case_instance_id
        process_definition_name = self.process_definition_name
        process_definition_key = self.process_definition_key
        process_definition_version = self.process_definition_version
        process_definition_id = self.process_definition_id
        business_key = self.business_key
        start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat() if self.start_time else None

        end_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat() if self.end_time else None

        removal_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.removal_time, Unset):
            removal_time = self.removal_time.isoformat() if self.removal_time else None

        duration_in_millis = self.duration_in_millis
        start_user_id = self.start_user_id
        start_activity_id = self.start_activity_id
        delete_reason = self.delete_reason
        tenant_id = self.tenant_id
        state: Union[Unset, None, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value if self.state else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if root_process_instance_id is not UNSET:
            field_dict["rootProcessInstanceId"] = root_process_instance_id
        if super_process_instance_id is not UNSET:
            field_dict["superProcessInstanceId"] = super_process_instance_id
        if super_case_instance_id is not UNSET:
            field_dict["superCaseInstanceId"] = super_case_instance_id
        if case_instance_id is not UNSET:
            field_dict["caseInstanceId"] = case_instance_id
        if process_definition_name is not UNSET:
            field_dict["processDefinitionName"] = process_definition_name
        if process_definition_key is not UNSET:
            field_dict["processDefinitionKey"] = process_definition_key
        if process_definition_version is not UNSET:
            field_dict["processDefinitionVersion"] = process_definition_version
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if business_key is not UNSET:
            field_dict["businessKey"] = business_key
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if removal_time is not UNSET:
            field_dict["removalTime"] = removal_time
        if duration_in_millis is not UNSET:
            field_dict["durationInMillis"] = duration_in_millis
        if start_user_id is not UNSET:
            field_dict["startUserId"] = start_user_id
        if start_activity_id is not UNSET:
            field_dict["startActivityId"] = start_activity_id
        if delete_reason is not UNSET:
            field_dict["deleteReason"] = delete_reason
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        root_process_instance_id = d.pop("rootProcessInstanceId", UNSET)

        super_process_instance_id = d.pop("superProcessInstanceId", UNSET)

        super_case_instance_id = d.pop("superCaseInstanceId", UNSET)

        case_instance_id = d.pop("caseInstanceId", UNSET)

        process_definition_name = d.pop("processDefinitionName", UNSET)

        process_definition_key = d.pop("processDefinitionKey", UNSET)

        process_definition_version = d.pop("processDefinitionVersion", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        business_key = d.pop("businessKey", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, None, datetime.datetime]
        if _start_time is None:
            start_time = None
        elif isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, None, datetime.datetime]
        if _end_time is None:
            end_time = None
        elif isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        _removal_time = d.pop("removalTime", UNSET)
        removal_time: Union[Unset, None, datetime.datetime]
        if _removal_time is None:
            removal_time = None
        elif isinstance(_removal_time, Unset):
            removal_time = UNSET
        else:
            removal_time = isoparse(_removal_time)

        duration_in_millis = d.pop("durationInMillis", UNSET)

        start_user_id = d.pop("startUserId", UNSET)

        start_activity_id = d.pop("startActivityId", UNSET)

        delete_reason = d.pop("deleteReason", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, None, HistoricProcessInstanceDtoState]
        if _state is None:
            state = None
        elif isinstance(_state, Unset):
            state = UNSET
        else:
            state = HistoricProcessInstanceDtoState(_state)

        historic_process_instance_dto = cls(
            id=id,
            root_process_instance_id=root_process_instance_id,
            super_process_instance_id=super_process_instance_id,
            super_case_instance_id=super_case_instance_id,
            case_instance_id=case_instance_id,
            process_definition_name=process_definition_name,
            process_definition_key=process_definition_key,
            process_definition_version=process_definition_version,
            process_definition_id=process_definition_id,
            business_key=business_key,
            start_time=start_time,
            end_time=end_time,
            removal_time=removal_time,
            duration_in_millis=duration_in_millis,
            start_user_id=start_user_id,
            start_activity_id=start_activity_id,
            delete_reason=delete_reason,
            tenant_id=tenant_id,
            state=state,
        )

        historic_process_instance_dto.additional_properties = d
        return historic_process_instance_dto

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
