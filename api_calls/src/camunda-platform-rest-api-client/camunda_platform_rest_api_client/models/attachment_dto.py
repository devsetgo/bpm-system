import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.atom_link import AtomLink
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentDto")


@attr.s(auto_attribs=True)
class AttachmentDto:
    """ """

    links: Union[Unset, None, List[AtomLink]] = UNSET
    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    task_id: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    create_time: Union[Unset, None, datetime.datetime] = UNSET
    removal_time: Union[Unset, None, datetime.datetime] = UNSET
    root_process_instance_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        id = self.id
        name = self.name
        description = self.description
        task_id = self.task_id
        type = self.type
        url = self.url
        create_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat() if self.create_time else None

        removal_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.removal_time, Unset):
            removal_time = self.removal_time.isoformat() if self.removal_time else None

        root_process_instance_id = self.root_process_instance_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if removal_time is not UNSET:
            field_dict["removalTime"] = removal_time
        if root_process_instance_id is not UNSET:
            field_dict["rootProcessInstanceId"] = root_process_instance_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = AtomLink.from_dict(links_item_data)

            links.append(links_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        task_id = d.pop("taskId", UNSET)

        type = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: Union[Unset, None, datetime.datetime]
        if _create_time is None:
            create_time = None
        elif isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = isoparse(_create_time)

        _removal_time = d.pop("removalTime", UNSET)
        removal_time: Union[Unset, None, datetime.datetime]
        if _removal_time is None:
            removal_time = None
        elif isinstance(_removal_time, Unset):
            removal_time = UNSET
        else:
            removal_time = isoparse(_removal_time)

        root_process_instance_id = d.pop("rootProcessInstanceId", UNSET)

        attachment_dto = cls(
            links=links,
            id=id,
            name=name,
            description=description,
            task_id=task_id,
            type=type,
            url=url,
            create_time=create_time,
            removal_time=removal_time,
            root_process_instance_id=root_process_instance_id,
        )

        attachment_dto.additional_properties = d
        return attachment_dto

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
