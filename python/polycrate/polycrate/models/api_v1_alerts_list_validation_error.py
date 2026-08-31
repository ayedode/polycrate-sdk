from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alerts_list_alert_router_error_component import ApiV1AlertsListAlertRouterErrorComponent
    from ..models.api_v1_alerts_list_category_error_component import ApiV1AlertsListCategoryErrorComponent
    from ..models.api_v1_alerts_list_created_after_error_component import ApiV1AlertsListCreatedAfterErrorComponent
    from ..models.api_v1_alerts_list_created_before_error_component import ApiV1AlertsListCreatedBeforeErrorComponent
    from ..models.api_v1_alerts_list_external_url_error_component import ApiV1AlertsListExternalUrlErrorComponent
    from ..models.api_v1_alerts_list_fingerprint_error_component import ApiV1AlertsListFingerprintErrorComponent
    from ..models.api_v1_alerts_list_name_error_component import ApiV1AlertsListNameErrorComponent
    from ..models.api_v1_alerts_list_organization_error_component import ApiV1AlertsListOrganizationErrorComponent
    from ..models.api_v1_alerts_list_original_alert_identifier_error_component import (
        ApiV1AlertsListOriginalAlertIdentifierErrorComponent,
    )
    from ..models.api_v1_alerts_list_since_error_component import ApiV1AlertsListSinceErrorComponent
    from ..models.api_v1_alerts_list_status_error_component import ApiV1AlertsListStatusErrorComponent
    from ..models.api_v1_alerts_list_until_error_component import ApiV1AlertsListUntilErrorComponent
    from ..models.api_v1_alerts_list_workspace_error_component import ApiV1AlertsListWorkspaceErrorComponent


T = TypeVar("T", bound="ApiV1AlertsListValidationError")


@_attrs_define
class ApiV1AlertsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertsListAlertRouterErrorComponent | ApiV1AlertsListCategoryErrorComponent |
            ApiV1AlertsListCreatedAfterErrorComponent | ApiV1AlertsListCreatedBeforeErrorComponent |
            ApiV1AlertsListExternalUrlErrorComponent | ApiV1AlertsListFingerprintErrorComponent |
            ApiV1AlertsListNameErrorComponent | ApiV1AlertsListOrganizationErrorComponent |
            ApiV1AlertsListOriginalAlertIdentifierErrorComponent | ApiV1AlertsListSinceErrorComponent |
            ApiV1AlertsListStatusErrorComponent | ApiV1AlertsListUntilErrorComponent |
            ApiV1AlertsListWorkspaceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertsListAlertRouterErrorComponent
        | ApiV1AlertsListCategoryErrorComponent
        | ApiV1AlertsListCreatedAfterErrorComponent
        | ApiV1AlertsListCreatedBeforeErrorComponent
        | ApiV1AlertsListExternalUrlErrorComponent
        | ApiV1AlertsListFingerprintErrorComponent
        | ApiV1AlertsListNameErrorComponent
        | ApiV1AlertsListOrganizationErrorComponent
        | ApiV1AlertsListOriginalAlertIdentifierErrorComponent
        | ApiV1AlertsListSinceErrorComponent
        | ApiV1AlertsListStatusErrorComponent
        | ApiV1AlertsListUntilErrorComponent
        | ApiV1AlertsListWorkspaceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alerts_list_alert_router_error_component import ApiV1AlertsListAlertRouterErrorComponent
        from ..models.api_v1_alerts_list_category_error_component import ApiV1AlertsListCategoryErrorComponent
        from ..models.api_v1_alerts_list_created_after_error_component import ApiV1AlertsListCreatedAfterErrorComponent
        from ..models.api_v1_alerts_list_created_before_error_component import (
            ApiV1AlertsListCreatedBeforeErrorComponent,
        )
        from ..models.api_v1_alerts_list_external_url_error_component import ApiV1AlertsListExternalUrlErrorComponent
        from ..models.api_v1_alerts_list_fingerprint_error_component import ApiV1AlertsListFingerprintErrorComponent
        from ..models.api_v1_alerts_list_name_error_component import ApiV1AlertsListNameErrorComponent
        from ..models.api_v1_alerts_list_organization_error_component import ApiV1AlertsListOrganizationErrorComponent
        from ..models.api_v1_alerts_list_original_alert_identifier_error_component import (
            ApiV1AlertsListOriginalAlertIdentifierErrorComponent,
        )
        from ..models.api_v1_alerts_list_since_error_component import ApiV1AlertsListSinceErrorComponent
        from ..models.api_v1_alerts_list_status_error_component import ApiV1AlertsListStatusErrorComponent
        from ..models.api_v1_alerts_list_workspace_error_component import ApiV1AlertsListWorkspaceErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListExternalUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListAlertRouterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListCategoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListOriginalAlertIdentifierErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListFingerprintErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListCreatedAfterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListCreatedBeforeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsListSinceErrorComponent):
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
        from ..models.api_v1_alerts_list_alert_router_error_component import ApiV1AlertsListAlertRouterErrorComponent
        from ..models.api_v1_alerts_list_category_error_component import ApiV1AlertsListCategoryErrorComponent
        from ..models.api_v1_alerts_list_created_after_error_component import ApiV1AlertsListCreatedAfterErrorComponent
        from ..models.api_v1_alerts_list_created_before_error_component import (
            ApiV1AlertsListCreatedBeforeErrorComponent,
        )
        from ..models.api_v1_alerts_list_external_url_error_component import ApiV1AlertsListExternalUrlErrorComponent
        from ..models.api_v1_alerts_list_fingerprint_error_component import ApiV1AlertsListFingerprintErrorComponent
        from ..models.api_v1_alerts_list_name_error_component import ApiV1AlertsListNameErrorComponent
        from ..models.api_v1_alerts_list_organization_error_component import ApiV1AlertsListOrganizationErrorComponent
        from ..models.api_v1_alerts_list_original_alert_identifier_error_component import (
            ApiV1AlertsListOriginalAlertIdentifierErrorComponent,
        )
        from ..models.api_v1_alerts_list_since_error_component import ApiV1AlertsListSinceErrorComponent
        from ..models.api_v1_alerts_list_status_error_component import ApiV1AlertsListStatusErrorComponent
        from ..models.api_v1_alerts_list_until_error_component import ApiV1AlertsListUntilErrorComponent
        from ..models.api_v1_alerts_list_workspace_error_component import ApiV1AlertsListWorkspaceErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertsListAlertRouterErrorComponent
                | ApiV1AlertsListCategoryErrorComponent
                | ApiV1AlertsListCreatedAfterErrorComponent
                | ApiV1AlertsListCreatedBeforeErrorComponent
                | ApiV1AlertsListExternalUrlErrorComponent
                | ApiV1AlertsListFingerprintErrorComponent
                | ApiV1AlertsListNameErrorComponent
                | ApiV1AlertsListOrganizationErrorComponent
                | ApiV1AlertsListOriginalAlertIdentifierErrorComponent
                | ApiV1AlertsListSinceErrorComponent
                | ApiV1AlertsListStatusErrorComponent
                | ApiV1AlertsListUntilErrorComponent
                | ApiV1AlertsListWorkspaceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_0 = ApiV1AlertsListNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_1 = (
                        ApiV1AlertsListOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_2 = (
                        ApiV1AlertsListWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_3 = ApiV1AlertsListStatusErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_4 = (
                        ApiV1AlertsListExternalUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_5 = (
                        ApiV1AlertsListAlertRouterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_6 = ApiV1AlertsListCategoryErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_7 = (
                        ApiV1AlertsListOriginalAlertIdentifierErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_8 = (
                        ApiV1AlertsListFingerprintErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_9 = (
                        ApiV1AlertsListCreatedAfterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_10 = (
                        ApiV1AlertsListCreatedBeforeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_list_error_type_11 = ApiV1AlertsListSinceErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_alerts_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alerts_list_error_type_12 = ApiV1AlertsListUntilErrorComponent.from_dict(data)

                return componentsschemas_api_v1_alerts_list_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alerts_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alerts_list_validation_error.additional_properties = d
        return api_v1_alerts_list_validation_error

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
