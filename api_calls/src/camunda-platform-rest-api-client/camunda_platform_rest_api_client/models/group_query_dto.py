from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.group_query_dto_sorting_item import GroupQueryDtoSortingItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupQueryDto")


@attr.s(auto_attribs=True)
class GroupQueryDto:
    """A group instance query which defines a list of group instances"""

    id: Union[Unset, None, str] = UNSET
    id_in: Union[Unset, None, List[str]] = UNSET
    name: Union[Unset, None, str] = UNSET
    name_like: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    member: Union[Unset, None, str] = UNSET
    member_of_tenant: Union[Unset, None, str] = UNSET
    sorting: Union[Unset, List[GroupQueryDtoSortingItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.id_in, Unset):
            if self.id_in is None:
                id_in = None
            else:
                id_in = self.id_in

        name = self.name
        name_like = self.name_like
        type = self.type
        member = self.member
        member_of_tenant = self.member_of_tenant
        sorting: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sorting, Unset):
            sorting = []
            for sorting_item_data in self.sorting:
                sorting_item = sorting_item_data.to_dict()

                sorting.append(sorting_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if id_in is not UNSET:
            field_dict["idIn"] = id_in
        if name is not UNSET:
            field_dict["name"] = name
        if name_like is not UNSET:
            field_dict["nameLike"] = name_like
        if type is not UNSET:
            field_dict["type"] = type
        if member is not UNSET:
            field_dict["member"] = member
        if member_of_tenant is not UNSET:
            field_dict["memberOfTenant"] = member_of_tenant
        if sorting is not UNSET:
            field_dict["sorting"] = sorting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        id_in = cast(List[str], d.pop("idIn", UNSET))

        name = d.pop("name", UNSET)

        name_like = d.pop("nameLike", UNSET)

        type = d.pop("type", UNSET)

        member = d.pop("member", UNSET)

        member_of_tenant = d.pop("memberOfTenant", UNSET)

        sorting = []
        _sorting = d.pop("sorting", UNSET)
        for sorting_item_data in _sorting or []:
            sorting_item = GroupQueryDtoSortingItem.from_dict(sorting_item_data)

            sorting.append(sorting_item)

        group_query_dto = cls(
            id=id,
            id_in=id_in,
            name=name,
            name_like=name_like,
            type=type,
            member=member,
            member_of_tenant=member_of_tenant,
            sorting=sorting,
        )

        group_query_dto.additional_properties = d
        return group_query_dto

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
