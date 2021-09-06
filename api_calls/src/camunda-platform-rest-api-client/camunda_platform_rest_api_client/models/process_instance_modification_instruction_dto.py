from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.process_instance_modification_instruction_dto_type import ProcessInstanceModificationInstructionDtoType
from ..models.trigger_variable_value_dto import TriggerVariableValueDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessInstanceModificationInstructionDto")


@attr.s(auto_attribs=True)
class ProcessInstanceModificationInstructionDto:
    """ """

    type: ProcessInstanceModificationInstructionDtoType
    variables: Union[Unset, TriggerVariableValueDto] = UNSET
    activity_id: Union[Unset, None, str] = UNSET
    transition_id: Union[Unset, None, str] = UNSET
    activity_instance_id: Union[Unset, None, str] = UNSET
    transition_instance_id: Union[Unset, None, str] = UNSET
    ancestor_activity_instance_id: Union[Unset, None, str] = UNSET
    cancel_current_active_activity_instances: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        variables: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        activity_id = self.activity_id
        transition_id = self.transition_id
        activity_instance_id = self.activity_instance_id
        transition_instance_id = self.transition_instance_id
        ancestor_activity_instance_id = self.ancestor_activity_instance_id
        cancel_current_active_activity_instances = self.cancel_current_active_activity_instances

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if variables is not UNSET:
            field_dict["variables"] = variables
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if transition_id is not UNSET:
            field_dict["transitionId"] = transition_id
        if activity_instance_id is not UNSET:
            field_dict["activityInstanceId"] = activity_instance_id
        if transition_instance_id is not UNSET:
            field_dict["transitionInstanceId"] = transition_instance_id
        if ancestor_activity_instance_id is not UNSET:
            field_dict["ancestorActivityInstanceId"] = ancestor_activity_instance_id
        if cancel_current_active_activity_instances is not UNSET:
            field_dict["cancelCurrentActiveActivityInstances"] = cancel_current_active_activity_instances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ProcessInstanceModificationInstructionDtoType(d.pop("type"))

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, TriggerVariableValueDto]
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = TriggerVariableValueDto.from_dict(_variables)

        activity_id = d.pop("activityId", UNSET)

        transition_id = d.pop("transitionId", UNSET)

        activity_instance_id = d.pop("activityInstanceId", UNSET)

        transition_instance_id = d.pop("transitionInstanceId", UNSET)

        ancestor_activity_instance_id = d.pop("ancestorActivityInstanceId", UNSET)

        cancel_current_active_activity_instances = d.pop("cancelCurrentActiveActivityInstances", UNSET)

        process_instance_modification_instruction_dto = cls(
            type=type,
            variables=variables,
            activity_id=activity_id,
            transition_id=transition_id,
            activity_instance_id=activity_instance_id,
            transition_instance_id=transition_instance_id,
            ancestor_activity_instance_id=ancestor_activity_instance_id,
            cancel_current_active_activity_instances=cancel_current_active_activity_instances,
        )

        process_instance_modification_instruction_dto.additional_properties = d
        return process_instance_modification_instruction_dto

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
