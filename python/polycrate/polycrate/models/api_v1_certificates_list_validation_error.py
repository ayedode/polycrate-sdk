from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_certificates_list_certificate_status_error_component import (
        ApiV1CertificatesListCertificateStatusErrorComponent,
    )
    from ..models.api_v1_certificates_list_created_by_users_error_component import (
        ApiV1CertificatesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_certificates_list_k8s_app_error_component import ApiV1CertificatesListK8SAppErrorComponent
    from ..models.api_v1_certificates_list_kind_error_component import ApiV1CertificatesListKindErrorComponent
    from ..models.api_v1_certificates_list_name_exact_error_component import (
        ApiV1CertificatesListNameExactErrorComponent,
    )
    from ..models.api_v1_certificates_list_organizations_error_component import (
        ApiV1CertificatesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_certificates_list_search_error_component import ApiV1CertificatesListSearchErrorComponent
    from ..models.api_v1_certificates_list_state_error_component import ApiV1CertificatesListStateErrorComponent
    from ..models.api_v1_certificates_list_state_not_error_component import ApiV1CertificatesListStateNotErrorComponent
    from ..models.api_v1_certificates_list_time_range_error_component import (
        ApiV1CertificatesListTimeRangeErrorComponent,
    )
    from ..models.api_v1_certificates_list_workspaces_error_component import (
        ApiV1CertificatesListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CertificatesListValidationError")


@_attrs_define
class ApiV1CertificatesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CertificatesListCertificateStatusErrorComponent |
            ApiV1CertificatesListCreatedByUsersErrorComponent | ApiV1CertificatesListK8SAppErrorComponent |
            ApiV1CertificatesListKindErrorComponent | ApiV1CertificatesListNameExactErrorComponent |
            ApiV1CertificatesListOrganizationsErrorComponent | ApiV1CertificatesListSearchErrorComponent |
            ApiV1CertificatesListStateErrorComponent | ApiV1CertificatesListStateNotErrorComponent |
            ApiV1CertificatesListTimeRangeErrorComponent | ApiV1CertificatesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CertificatesListCertificateStatusErrorComponent
        | ApiV1CertificatesListCreatedByUsersErrorComponent
        | ApiV1CertificatesListK8SAppErrorComponent
        | ApiV1CertificatesListKindErrorComponent
        | ApiV1CertificatesListNameExactErrorComponent
        | ApiV1CertificatesListOrganizationsErrorComponent
        | ApiV1CertificatesListSearchErrorComponent
        | ApiV1CertificatesListStateErrorComponent
        | ApiV1CertificatesListStateNotErrorComponent
        | ApiV1CertificatesListTimeRangeErrorComponent
        | ApiV1CertificatesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_certificates_list_certificate_status_error_component import (
            ApiV1CertificatesListCertificateStatusErrorComponent,
        )
        from ..models.api_v1_certificates_list_created_by_users_error_component import (
            ApiV1CertificatesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_certificates_list_kind_error_component import ApiV1CertificatesListKindErrorComponent
        from ..models.api_v1_certificates_list_name_exact_error_component import (
            ApiV1CertificatesListNameExactErrorComponent,
        )
        from ..models.api_v1_certificates_list_organizations_error_component import (
            ApiV1CertificatesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_certificates_list_search_error_component import ApiV1CertificatesListSearchErrorComponent
        from ..models.api_v1_certificates_list_state_error_component import ApiV1CertificatesListStateErrorComponent
        from ..models.api_v1_certificates_list_state_not_error_component import (
            ApiV1CertificatesListStateNotErrorComponent,
        )
        from ..models.api_v1_certificates_list_time_range_error_component import (
            ApiV1CertificatesListTimeRangeErrorComponent,
        )
        from ..models.api_v1_certificates_list_workspaces_error_component import (
            ApiV1CertificatesListWorkspacesErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CertificatesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesListNameExactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CertificatesListCertificateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_certificates_list_certificate_status_error_component import (
            ApiV1CertificatesListCertificateStatusErrorComponent,
        )
        from ..models.api_v1_certificates_list_created_by_users_error_component import (
            ApiV1CertificatesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_certificates_list_k8s_app_error_component import ApiV1CertificatesListK8SAppErrorComponent
        from ..models.api_v1_certificates_list_kind_error_component import ApiV1CertificatesListKindErrorComponent
        from ..models.api_v1_certificates_list_name_exact_error_component import (
            ApiV1CertificatesListNameExactErrorComponent,
        )
        from ..models.api_v1_certificates_list_organizations_error_component import (
            ApiV1CertificatesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_certificates_list_search_error_component import ApiV1CertificatesListSearchErrorComponent
        from ..models.api_v1_certificates_list_state_error_component import ApiV1CertificatesListStateErrorComponent
        from ..models.api_v1_certificates_list_state_not_error_component import (
            ApiV1CertificatesListStateNotErrorComponent,
        )
        from ..models.api_v1_certificates_list_time_range_error_component import (
            ApiV1CertificatesListTimeRangeErrorComponent,
        )
        from ..models.api_v1_certificates_list_workspaces_error_component import (
            ApiV1CertificatesListWorkspacesErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CertificatesListCertificateStatusErrorComponent
                | ApiV1CertificatesListCreatedByUsersErrorComponent
                | ApiV1CertificatesListK8SAppErrorComponent
                | ApiV1CertificatesListKindErrorComponent
                | ApiV1CertificatesListNameExactErrorComponent
                | ApiV1CertificatesListOrganizationsErrorComponent
                | ApiV1CertificatesListSearchErrorComponent
                | ApiV1CertificatesListStateErrorComponent
                | ApiV1CertificatesListStateNotErrorComponent
                | ApiV1CertificatesListTimeRangeErrorComponent
                | ApiV1CertificatesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_list_error_type_0 = (
                        ApiV1CertificatesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_list_error_type_1 = (
                        ApiV1CertificatesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_list_error_type_2 = (
                        ApiV1CertificatesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_list_error_type_3 = (
                        ApiV1CertificatesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_list_error_type_4 = (
                        ApiV1CertificatesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_list_error_type_5 = (
                        ApiV1CertificatesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_list_error_type_6 = (
                        ApiV1CertificatesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_list_error_type_7 = (
                        ApiV1CertificatesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_list_error_type_8 = (
                        ApiV1CertificatesListNameExactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_certificates_list_error_type_9 = (
                        ApiV1CertificatesListCertificateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_certificates_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_certificates_list_error_type_10 = (
                    ApiV1CertificatesListK8SAppErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_certificates_list_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_certificates_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_certificates_list_validation_error.additional_properties = d
        return api_v1_certificates_list_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
