from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.process_instance_modification_instruction_dto import ProcessInstanceModificationInstructionDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessInstanceModificationDto")


@attr.s(auto_attribs=True)
class ProcessInstanceModificationDto:
    """ """

    skip_custom_listeners: Union[Unset, None, bool] = UNSET
    skip_io_mappings: Union[Unset, None, bool] = UNSET
    instructions: Union[Unset, None, List[ProcessInstanceModificationInstructionDto]] = UNSET
    annotation: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        skip_custom_listeners = self.skip_custom_listeners
        skip_io_mappings = self.skip_io_mappings
        instructions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.instructions, Unset):
            if self.instructions is None:
                instructions = None
            else:
                instructions = []
                for instructions_item_data in self.instructions:
                    instructions_item = instructions_item_data.to_dict()

                    instructions.append(instructions_item)

        annotation = self.annotation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if skip_custom_listeners is not UNSET:
            field_dict["skipCustomListeners"] = skip_custom_listeners
        if skip_io_mappings is not UNSET:
            field_dict["skipIoMappings"] = skip_io_mappings
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if annotation is not UNSET:
            field_dict["annotation"] = annotation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        skip_custom_listeners = d.pop("skipCustomListeners", UNSET)

        skip_io_mappings = d.pop("skipIoMappings", UNSET)

        instructions = []
        _instructions = d.pop("instructions", UNSET)
        for instructions_item_data in _instructions or []:
            instructions_item = ProcessInstanceModificationInstructionDto.from_dict(instructions_item_data)

            instructions.append(instructions_item)

        annotation = d.pop("annotation", UNSET)

        process_instance_modification_dto = cls(
            skip_custom_listeners=skip_custom_listeners,
            skip_io_mappings=skip_io_mappings,
            instructions=instructions,
            annotation=annotation,
        )

        process_instance_modification_dto.additional_properties = d
        return process_instance_modification_dto

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
