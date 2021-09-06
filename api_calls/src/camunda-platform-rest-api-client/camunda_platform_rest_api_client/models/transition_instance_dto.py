from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.activity_instance_incident_dto import ActivityInstanceIncidentDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransitionInstanceDto")


@attr.s(auto_attribs=True)
class TransitionInstanceDto:
    """A JSON object corresponding to the Activity Instance tree of the given process instance."""

    id: Union[Unset, None, str] = UNSET
    parent_activity_instance_id: Union[Unset, None, str] = UNSET
    activity_id: Union[Unset, None, str] = UNSET
    activity_name: Union[Unset, None, str] = UNSET
    activity_type: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    incident_ids: Union[Unset, None, List[str]] = UNSET
    incidents: Union[Unset, None, List[ActivityInstanceIncidentDto]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parent_activity_instance_id = self.parent_activity_instance_id
        activity_id = self.activity_id
        activity_name = self.activity_name
        activity_type = self.activity_type
        process_instance_id = self.process_instance_id
        process_definition_id = self.process_definition_id
        execution_id = self.execution_id
        incident_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.incident_ids, Unset):
            if self.incident_ids is None:
                incident_ids = None
            else:
                incident_ids = self.incident_ids

        incidents: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.incidents, Unset):
            if self.incidents is None:
                incidents = None
            else:
                incidents = []
                for incidents_item_data in self.incidents:
                    incidents_item = incidents_item_data.to_dict()

                    incidents.append(incidents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parent_activity_instance_id is not UNSET:
            field_dict["parentActivityInstanceId"] = parent_activity_instance_id
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if activity_name is not UNSET:
            field_dict["activityName"] = activity_name
        if activity_type is not UNSET:
            field_dict["activityType"] = activity_type
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if incident_ids is not UNSET:
            field_dict["incidentIds"] = incident_ids
        if incidents is not UNSET:
            field_dict["incidents"] = incidents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        parent_activity_instance_id = d.pop("parentActivityInstanceId", UNSET)

        activity_id = d.pop("activityId", UNSET)

        activity_name = d.pop("activityName", UNSET)

        activity_type = d.pop("activityType", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        execution_id = d.pop("executionId", UNSET)

        incident_ids = cast(List[str], d.pop("incidentIds", UNSET))

        incidents = []
        _incidents = d.pop("incidents", UNSET)
        for incidents_item_data in _incidents or []:
            incidents_item = ActivityInstanceIncidentDto.from_dict(incidents_item_data)

            incidents.append(incidents_item)

        transition_instance_dto = cls(
            id=id,
            parent_activity_instance_id=parent_activity_instance_id,
            activity_id=activity_id,
            activity_name=activity_name,
            activity_type=activity_type,
            process_instance_id=process_instance_id,
            process_definition_id=process_definition_id,
            execution_id=execution_id,
            incident_ids=incident_ids,
            incidents=incidents,
        )

        transition_instance_dto.additional_properties = d
        return transition_instance_dto

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
