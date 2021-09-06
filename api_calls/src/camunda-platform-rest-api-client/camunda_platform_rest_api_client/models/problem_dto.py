from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProblemDto")


@attr.s(auto_attribs=True)
class ProblemDto:
    """ """

    message: Union[Unset, None, str] = UNSET
    line: Union[Unset, None, int] = UNSET
    column: Union[Unset, None, int] = UNSET
    main_element_id: Union[Unset, None, str] = UNSET
    element_ids: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        line = self.line
        column = self.column
        main_element_id = self.main_element_id
        element_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.element_ids, Unset):
            if self.element_ids is None:
                element_ids = None
            else:
                element_ids = self.element_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if line is not UNSET:
            field_dict["line"] = line
        if column is not UNSET:
            field_dict["column"] = column
        if main_element_id is not UNSET:
            field_dict["mainElementId"] = main_element_id
        if element_ids is not UNSET:
            field_dict["elementIds"] = element_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        line = d.pop("line", UNSET)

        column = d.pop("column", UNSET)

        main_element_id = d.pop("mainElementId", UNSET)

        element_ids = cast(List[str], d.pop("elementIds", UNSET))

        problem_dto = cls(
            message=message,
            line=line,
            column=column,
            main_element_id=main_element_id,
            element_ids=element_ids,
        )

        problem_dto.additional_properties = d
        return problem_dto

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
