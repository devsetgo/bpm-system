import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentDto")


@attr.s(auto_attribs=True)
class IncidentDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    incident_timestamp: Union[Unset, None, datetime.datetime] = UNSET
    incident_type: Union[Unset, None, str] = UNSET
    activity_id: Union[Unset, None, str] = UNSET
    failed_activity_id: Union[Unset, None, str] = UNSET
    cause_incident_id: Union[Unset, None, str] = UNSET
    root_cause_incident_id: Union[Unset, None, str] = UNSET
    configuration: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    incident_message: Union[Unset, None, str] = UNSET
    job_definition_id: Union[Unset, None, str] = UNSET
    annotation: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        process_definition_id = self.process_definition_id
        process_instance_id = self.process_instance_id
        execution_id = self.execution_id
        incident_timestamp: Union[Unset, None, str] = UNSET
        if not isinstance(self.incident_timestamp, Unset):
            incident_timestamp = self.incident_timestamp.isoformat() if self.incident_timestamp else None

        incident_type = self.incident_type
        activity_id = self.activity_id
        failed_activity_id = self.failed_activity_id
        cause_incident_id = self.cause_incident_id
        root_cause_incident_id = self.root_cause_incident_id
        configuration = self.configuration
        tenant_id = self.tenant_id
        incident_message = self.incident_message
        job_definition_id = self.job_definition_id
        annotation = self.annotation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if incident_timestamp is not UNSET:
            field_dict["incidentTimestamp"] = incident_timestamp
        if incident_type is not UNSET:
            field_dict["incidentType"] = incident_type
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if failed_activity_id is not UNSET:
            field_dict["failedActivityId"] = failed_activity_id
        if cause_incident_id is not UNSET:
            field_dict["causeIncidentId"] = cause_incident_id
        if root_cause_incident_id is not UNSET:
            field_dict["rootCauseIncidentId"] = root_cause_incident_id
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if incident_message is not UNSET:
            field_dict["incidentMessage"] = incident_message
        if job_definition_id is not UNSET:
            field_dict["jobDefinitionId"] = job_definition_id
        if annotation is not UNSET:
            field_dict["annotation"] = annotation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        execution_id = d.pop("executionId", UNSET)

        _incident_timestamp = d.pop("incidentTimestamp", UNSET)
        incident_timestamp: Union[Unset, None, datetime.datetime]
        if _incident_timestamp is None:
            incident_timestamp = None
        elif isinstance(_incident_timestamp, Unset):
            incident_timestamp = UNSET
        else:
            incident_timestamp = isoparse(_incident_timestamp)

        incident_type = d.pop("incidentType", UNSET)

        activity_id = d.pop("activityId", UNSET)

        failed_activity_id = d.pop("failedActivityId", UNSET)

        cause_incident_id = d.pop("causeIncidentId", UNSET)

        root_cause_incident_id = d.pop("rootCauseIncidentId", UNSET)

        configuration = d.pop("configuration", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        incident_message = d.pop("incidentMessage", UNSET)

        job_definition_id = d.pop("jobDefinitionId", UNSET)

        annotation = d.pop("annotation", UNSET)

        incident_dto = cls(
            id=id,
            process_definition_id=process_definition_id,
            process_instance_id=process_instance_id,
            execution_id=execution_id,
            incident_timestamp=incident_timestamp,
            incident_type=incident_type,
            activity_id=activity_id,
            failed_activity_id=failed_activity_id,
            cause_incident_id=cause_incident_id,
            root_cause_incident_id=root_cause_incident_id,
            configuration=configuration,
            tenant_id=tenant_id,
            incident_message=incident_message,
            job_definition_id=job_definition_id,
            annotation=annotation,
        )

        incident_dto.additional_properties = d
        return incident_dto

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
