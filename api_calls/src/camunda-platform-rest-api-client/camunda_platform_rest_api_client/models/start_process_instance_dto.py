from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.process_instance_modification_instruction_dto import ProcessInstanceModificationInstructionDto
from ..models.start_process_instance_dto_variables import StartProcessInstanceDtoVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="StartProcessInstanceDto")


@attr.s(auto_attribs=True)
class StartProcessInstanceDto:
    """ """

    business_key: Union[Unset, None, str] = UNSET
    variables: Union[Unset, None, StartProcessInstanceDtoVariables] = UNSET
    case_instance_id: Union[Unset, None, str] = UNSET
    start_instructions: Union[Unset, None, List[ProcessInstanceModificationInstructionDto]] = UNSET
    skip_custom_listeners: Union[Unset, None, bool] = UNSET
    skip_io_mappings: Union[Unset, None, bool] = UNSET
    with_variables_in_return: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_key = self.business_key
        variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict() if self.variables else None

        case_instance_id = self.case_instance_id
        start_instructions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.start_instructions, Unset):
            if self.start_instructions is None:
                start_instructions = None
            else:
                start_instructions = []
                for start_instructions_item_data in self.start_instructions:
                    start_instructions_item = start_instructions_item_data.to_dict()

                    start_instructions.append(start_instructions_item)

        skip_custom_listeners = self.skip_custom_listeners
        skip_io_mappings = self.skip_io_mappings
        with_variables_in_return = self.with_variables_in_return

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_key is not UNSET:
            field_dict["businessKey"] = business_key
        if variables is not UNSET:
            field_dict["variables"] = variables
        if case_instance_id is not UNSET:
            field_dict["caseInstanceId"] = case_instance_id
        if start_instructions is not UNSET:
            field_dict["startInstructions"] = start_instructions
        if skip_custom_listeners is not UNSET:
            field_dict["skipCustomListeners"] = skip_custom_listeners
        if skip_io_mappings is not UNSET:
            field_dict["skipIoMappings"] = skip_io_mappings
        if with_variables_in_return is not UNSET:
            field_dict["withVariablesInReturn"] = with_variables_in_return

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        business_key = d.pop("businessKey", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, StartProcessInstanceDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = StartProcessInstanceDtoVariables.from_dict(_variables)

        case_instance_id = d.pop("caseInstanceId", UNSET)

        start_instructions = []
        _start_instructions = d.pop("startInstructions", UNSET)
        for start_instructions_item_data in _start_instructions or []:
            start_instructions_item = ProcessInstanceModificationInstructionDto.from_dict(start_instructions_item_data)

            start_instructions.append(start_instructions_item)

        skip_custom_listeners = d.pop("skipCustomListeners", UNSET)

        skip_io_mappings = d.pop("skipIoMappings", UNSET)

        with_variables_in_return = d.pop("withVariablesInReturn", UNSET)

        start_process_instance_dto = cls(
            business_key=business_key,
            variables=variables,
            case_instance_id=case_instance_id,
            start_instructions=start_instructions,
            skip_custom_listeners=skip_custom_listeners,
            skip_io_mappings=skip_io_mappings,
            with_variables_in_return=with_variables_in_return,
        )

        start_process_instance_dto.additional_properties = d
        return start_process_instance_dto

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
