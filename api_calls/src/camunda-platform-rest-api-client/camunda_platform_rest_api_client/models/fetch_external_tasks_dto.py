from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.fetch_external_task_topic_dto import FetchExternalTaskTopicDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="FetchExternalTasksDto")


@attr.s(auto_attribs=True)
class FetchExternalTasksDto:
    """ """

    worker_id: str
    max_tasks: Optional[int]
    use_priority: Union[Unset, None, bool] = UNSET
    async_response_timeout: Union[Unset, None, int] = UNSET
    topics: Union[Unset, None, List[FetchExternalTaskTopicDto]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        worker_id = self.worker_id
        max_tasks = self.max_tasks
        use_priority = self.use_priority
        async_response_timeout = self.async_response_timeout
        topics: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.topics, Unset):
            if self.topics is None:
                topics = None
            else:
                topics = []
                for topics_item_data in self.topics:
                    topics_item = topics_item_data.to_dict()

                    topics.append(topics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workerId": worker_id,
                "maxTasks": max_tasks,
            }
        )
        if use_priority is not UNSET:
            field_dict["usePriority"] = use_priority
        if async_response_timeout is not UNSET:
            field_dict["asyncResponseTimeout"] = async_response_timeout
        if topics is not UNSET:
            field_dict["topics"] = topics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        worker_id = d.pop("workerId")

        max_tasks = d.pop("maxTasks")

        use_priority = d.pop("usePriority", UNSET)

        async_response_timeout = d.pop("asyncResponseTimeout", UNSET)

        topics = []
        _topics = d.pop("topics", UNSET)
        for topics_item_data in _topics or []:
            topics_item = FetchExternalTaskTopicDto.from_dict(topics_item_data)

            topics.append(topics_item)

        fetch_external_tasks_dto = cls(
            worker_id=worker_id,
            max_tasks=max_tasks,
            use_priority=use_priority,
            async_response_timeout=async_response_timeout,
            topics=topics,
        )

        fetch_external_tasks_dto.additional_properties = d
        return fetch_external_tasks_dto

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
