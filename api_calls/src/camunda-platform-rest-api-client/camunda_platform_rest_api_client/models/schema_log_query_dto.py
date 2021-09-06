from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.schema_log_query_dto_sorting_item import SchemaLogQueryDtoSortingItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaLogQueryDto")


@attr.s(auto_attribs=True)
class SchemaLogQueryDto:
    """ """

    version: Union[Unset, None, str] = UNSET
    sorting: Union[Unset, List[SchemaLogQueryDtoSortingItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        sorting: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sorting, Unset):
            sorting = []
            for sorting_item_data in self.sorting:
                sorting_item = sorting_item_data.to_dict()

                sorting.append(sorting_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if sorting is not UNSET:
            field_dict["sorting"] = sorting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        sorting = []
        _sorting = d.pop("sorting", UNSET)
        for sorting_item_data in _sorting or []:
            sorting_item = SchemaLogQueryDtoSortingItem.from_dict(sorting_item_data)

            sorting.append(sorting_item)

        schema_log_query_dto = cls(
            version=version,
            sorting=sorting,
        )

        schema_log_query_dto.additional_properties = d
        return schema_log_query_dto

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
