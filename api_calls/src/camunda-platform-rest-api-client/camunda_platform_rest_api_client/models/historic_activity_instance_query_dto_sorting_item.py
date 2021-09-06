from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.historic_activity_instance_query_dto_sorting_item_sort_by import (
    HistoricActivityInstanceQueryDtoSortingItemSortBy,
)
from ..models.historic_activity_instance_query_dto_sorting_item_sort_order import (
    HistoricActivityInstanceQueryDtoSortingItemSortOrder,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoricActivityInstanceQueryDtoSortingItem")


@attr.s(auto_attribs=True)
class HistoricActivityInstanceQueryDtoSortingItem:
    """ """

    sort_by: Union[Unset, None, HistoricActivityInstanceQueryDtoSortingItemSortBy] = UNSET
    sort_order: Union[Unset, None, HistoricActivityInstanceQueryDtoSortingItemSortOrder] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sort_by: Union[Unset, None, str] = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by.value if self.sort_by else None

        sort_order: Union[Unset, None, str] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value if self.sort_order else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sort_by = d.pop("sortBy", UNSET)
        sort_by: Union[Unset, None, HistoricActivityInstanceQueryDtoSortingItemSortBy]
        if _sort_by is None:
            sort_by = None
        elif isinstance(_sort_by, Unset):
            sort_by = UNSET
        else:
            sort_by = HistoricActivityInstanceQueryDtoSortingItemSortBy(_sort_by)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: Union[Unset, None, HistoricActivityInstanceQueryDtoSortingItemSortOrder]
        if _sort_order is None:
            sort_order = None
        elif isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = HistoricActivityInstanceQueryDtoSortingItemSortOrder(_sort_order)

        historic_activity_instance_query_dto_sorting_item = cls(
            sort_by=sort_by,
            sort_order=sort_order,
        )

        historic_activity_instance_query_dto_sorting_item.additional_properties = d
        return historic_activity_instance_query_dto_sorting_item

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
