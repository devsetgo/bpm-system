from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RedeploymentDto")


@attr.s(auto_attribs=True)
class RedeploymentDto:
    """A JSON object with the following properties:"""

    resource_ids: Union[Unset, None, List[str]] = UNSET
    resource_names: Union[Unset, None, List[str]] = UNSET
    source: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.resource_ids, Unset):
            if self.resource_ids is None:
                resource_ids = None
            else:
                resource_ids = self.resource_ids

        resource_names: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.resource_names, Unset):
            if self.resource_names is None:
                resource_names = None
            else:
                resource_names = self.resource_names

        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_ids is not UNSET:
            field_dict["resourceIds"] = resource_ids
        if resource_names is not UNSET:
            field_dict["resourceNames"] = resource_names
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resource_ids = cast(List[str], d.pop("resourceIds", UNSET))

        resource_names = cast(List[str], d.pop("resourceNames", UNSET))

        source = d.pop("source", UNSET)

        redeployment_dto = cls(
            resource_ids=resource_ids,
            resource_names=resource_names,
            source=source,
        )

        redeployment_dto.additional_properties = d
        return redeployment_dto

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
