from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AtomLink")


@attr.s(auto_attribs=True)
class AtomLink:
    """ """

    rel: Union[Unset, None, str] = UNSET
    href: Union[Unset, None, str] = UNSET
    method: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rel = self.rel
        href = self.href
        method = self.method

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rel is not UNSET:
            field_dict["rel"] = rel
        if href is not UNSET:
            field_dict["href"] = href
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rel = d.pop("rel", UNSET)

        href = d.pop("href", UNSET)

        method = d.pop("method", UNSET)

        atom_link = cls(
            rel=rel,
            href=href,
            method=method,
        )

        atom_link.additional_properties = d
        return atom_link

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
