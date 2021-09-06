from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessDefinitionDiagramDto")


@attr.s(auto_attribs=True)
class ProcessDefinitionDiagramDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    bpmn_20_xml: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        bpmn_20_xml = self.bpmn_20_xml

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if bpmn_20_xml is not UNSET:
            field_dict["bpmn20Xml"] = bpmn_20_xml

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        bpmn_20_xml = d.pop("bpmn20Xml", UNSET)

        process_definition_diagram_dto = cls(
            id=id,
            bpmn_20_xml=bpmn_20_xml,
        )

        process_definition_diagram_dto.additional_properties = d
        return process_definition_diagram_dto

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
