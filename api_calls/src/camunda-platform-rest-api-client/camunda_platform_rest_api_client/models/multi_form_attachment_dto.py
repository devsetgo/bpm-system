from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="MultiFormAttachmentDto")


@attr.s(auto_attribs=True)
class MultiFormAttachmentDto:
    """ """

    attachment_name: Union[Unset, None, str] = UNSET
    attachment_description: Union[Unset, None, str] = UNSET
    attachment_type: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    content: Union[Unset, None, File] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attachment_name = self.attachment_name
        attachment_description = self.attachment_description
        attachment_type = self.attachment_type
        url = self.url
        content: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_tuple() if self.content else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachment_name is not UNSET:
            field_dict["attachment-name"] = attachment_name
        if attachment_description is not UNSET:
            field_dict["attachment-description"] = attachment_description
        if attachment_type is not UNSET:
            field_dict["attachment-type"] = attachment_type
        if url is not UNSET:
            field_dict["url"] = url
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        attachment_name = (
            self.attachment_name if self.attachment_name is UNSET else (None, str(self.attachment_name), "text/plain")
        )
        attachment_description = (
            self.attachment_description
            if self.attachment_description is UNSET
            else (None, str(self.attachment_description), "text/plain")
        )
        attachment_type = (
            self.attachment_type if self.attachment_type is UNSET else (None, str(self.attachment_type), "text/plain")
        )
        url = self.url if self.url is UNSET else (None, str(self.url), "text/plain")
        content: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_tuple() if self.content else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        field_dict.update({})
        if attachment_name is not UNSET:
            field_dict["attachment-name"] = attachment_name
        if attachment_description is not UNSET:
            field_dict["attachment-description"] = attachment_description
        if attachment_type is not UNSET:
            field_dict["attachment-type"] = attachment_type
        if url is not UNSET:
            field_dict["url"] = url
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attachment_name = d.pop("attachment-name", UNSET)

        attachment_description = d.pop("attachment-description", UNSET)

        attachment_type = d.pop("attachment-type", UNSET)

        url = d.pop("url", UNSET)

        _content = d.pop("content", UNSET)
        content: Union[Unset, None, File]
        if _content is None:
            content = None
        elif isinstance(_content, Unset):
            content = UNSET
        else:
            content = File(payload=BytesIO(_content))

        multi_form_attachment_dto = cls(
            attachment_name=attachment_name,
            attachment_description=attachment_description,
            attachment_type=attachment_type,
            url=url,
            content=content,
        )

        multi_form_attachment_dto.additional_properties = d
        return multi_form_attachment_dto

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
