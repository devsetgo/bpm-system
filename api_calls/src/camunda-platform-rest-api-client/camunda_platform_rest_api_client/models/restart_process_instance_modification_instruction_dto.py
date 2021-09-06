from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.restart_process_instance_modification_instruction_dto_type import (
    RestartProcessInstanceModificationInstructionDtoType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestartProcessInstanceModificationInstructionDto")


@attr.s(auto_attribs=True)
class RestartProcessInstanceModificationInstructionDto:
    """ """

    type: RestartProcessInstanceModificationInstructionDtoType
    activity_id: Union[Unset, None, str] = UNSET
    transition_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        activity_id = self.activity_id
        transition_id = self.transition_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if transition_id is not UNSET:
            field_dict["transitionId"] = transition_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = RestartProcessInstanceModificationInstructionDtoType(d.pop("type"))

        activity_id = d.pop("activityId", UNSET)

        transition_id = d.pop("transitionId", UNSET)

        restart_process_instance_modification_instruction_dto = cls(
            type=type,
            activity_id=activity_id,
            transition_id=transition_id,
        )

        restart_process_instance_modification_instruction_dto.additional_properties = d
        return restart_process_instance_modification_instruction_dto

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
