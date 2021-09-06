from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.incident_statistics_result_dto import IncidentStatisticsResultDto
from ..models.process_definition_dto import ProcessDefinitionDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessDefinitionStatisticsResultDto")


@attr.s(auto_attribs=True)
class ProcessDefinitionStatisticsResultDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    instances: Union[Unset, int] = UNSET
    failed_jobs: Union[Unset, int] = UNSET
    incidents: Union[Unset, None, List[IncidentStatisticsResultDto]] = UNSET
    definition: Union[Unset, ProcessDefinitionDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        instances = self.instances
        failed_jobs = self.failed_jobs
        incidents: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.incidents, Unset):
            if self.incidents is None:
                incidents = None
            else:
                incidents = []
                for incidents_item_data in self.incidents:
                    incidents_item = incidents_item_data.to_dict()

                    incidents.append(incidents_item)

        definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.definition, Unset):
            definition = self.definition.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if instances is not UNSET:
            field_dict["instances"] = instances
        if failed_jobs is not UNSET:
            field_dict["failedJobs"] = failed_jobs
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if definition is not UNSET:
            field_dict["definition"] = definition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        instances = d.pop("instances", UNSET)

        failed_jobs = d.pop("failedJobs", UNSET)

        incidents = []
        _incidents = d.pop("incidents", UNSET)
        for incidents_item_data in _incidents or []:
            incidents_item = IncidentStatisticsResultDto.from_dict(incidents_item_data)

            incidents.append(incidents_item)

        _definition = d.pop("definition", UNSET)
        definition: Union[Unset, ProcessDefinitionDto]
        if isinstance(_definition, Unset):
            definition = UNSET
        else:
            definition = ProcessDefinitionDto.from_dict(_definition)

        process_definition_statistics_result_dto = cls(
            id=id,
            instances=instances,
            failed_jobs=failed_jobs,
            incidents=incidents,
            definition=definition,
        )

        process_definition_statistics_result_dto.additional_properties = d
        return process_definition_statistics_result_dto

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
