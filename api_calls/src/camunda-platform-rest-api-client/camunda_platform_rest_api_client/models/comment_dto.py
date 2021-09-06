import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.atom_link import AtomLink
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentDto")


@attr.s(auto_attribs=True)
class CommentDto:
    """ """

    links: Union[Unset, None, List[AtomLink]] = UNSET
    id: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    task_id: Union[Unset, None, str] = UNSET
    time: Union[Unset, None, datetime.datetime] = UNSET
    message: Union[Unset, None, str] = UNSET
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
        user_id = self.user_id
        task_id = self.task_id
        time: Union[Unset, None, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat() if self.time else None

        message = self.message
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
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if time is not UNSET:
            field_dict["time"] = time
        if message is not UNSET:
            field_dict["message"] = message
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

        user_id = d.pop("userId", UNSET)

        task_id = d.pop("taskId", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, None, datetime.datetime]
        if _time is None:
            time = None
        elif isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        message = d.pop("message", UNSET)

        _removal_time = d.pop("removalTime", UNSET)
        removal_time: Union[Unset, None, datetime.datetime]
        if _removal_time is None:
            removal_time = None
        elif isinstance(_removal_time, Unset):
            removal_time = UNSET
        else:
            removal_time = isoparse(_removal_time)

        root_process_instance_id = d.pop("rootProcessInstanceId", UNSET)

        comment_dto = cls(
            links=links,
            id=id,
            user_id=user_id,
            task_id=task_id,
            time=time,
            message=message,
            removal_time=removal_time,
            root_process_instance_id=root_process_instance_id,
        )

        comment_dto.additional_properties = d
        return comment_dto

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
