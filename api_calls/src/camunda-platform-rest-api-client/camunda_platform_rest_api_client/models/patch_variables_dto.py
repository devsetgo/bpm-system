from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.patch_variables_dto_modifications import PatchVariablesDtoModifications
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchVariablesDto")


@attr.s(auto_attribs=True)
class PatchVariablesDto:
    """ """

    modifications: Union[Unset, None, PatchVariablesDtoModifications] = UNSET
    deletions: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        modifications: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.modifications, Unset):
            modifications = self.modifications.to_dict() if self.modifications else None

        deletions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.deletions, Unset):
            if self.deletions is None:
                deletions = None
            else:
                deletions = self.deletions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modifications is not UNSET:
            field_dict["modifications"] = modifications
        if deletions is not UNSET:
            field_dict["deletions"] = deletions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _modifications = d.pop("modifications", UNSET)
        modifications: Union[Unset, None, PatchVariablesDtoModifications]
        if _modifications is None:
            modifications = None
        elif isinstance(_modifications, Unset):
            modifications = UNSET
        else:
            modifications = PatchVariablesDtoModifications.from_dict(_modifications)

        deletions = cast(List[str], d.pop("deletions", UNSET))

        patch_variables_dto = cls(
            modifications=modifications,
            deletions=deletions,
        )

        patch_variables_dto.additional_properties = d
        return patch_variables_dto

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
