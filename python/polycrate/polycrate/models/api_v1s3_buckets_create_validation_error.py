from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1s3_buckets_create_annotations_error_component import (
        ApiV1S3BucketsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1s3_buckets_create_cors_allow_all_error_component import (
        ApiV1S3BucketsCreateCorsAllowAllErrorComponent,
    )
    from ..models.api_v1s3_buckets_create_labels_error_component import ApiV1S3BucketsCreateLabelsErrorComponent
    from ..models.api_v1s3_buckets_create_name_error_component import ApiV1S3BucketsCreateNameErrorComponent
    from ..models.api_v1s3_buckets_create_non_field_errors_error_component import (
        ApiV1S3BucketsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1s3_buckets_create_organization_error_component import (
        ApiV1S3BucketsCreateOrganizationErrorComponent,
    )
    from ..models.api_v1s3_buckets_create_region_error_component import ApiV1S3BucketsCreateRegionErrorComponent
    from ..models.api_v1s3_buckets_create_workspace_error_component import ApiV1S3BucketsCreateWorkspaceErrorComponent


T = TypeVar("T", bound="ApiV1S3BucketsCreateValidationError")


@_attrs_define
class ApiV1S3BucketsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1S3BucketsCreateAnnotationsErrorComponent | ApiV1S3BucketsCreateCorsAllowAllErrorComponent |
            ApiV1S3BucketsCreateLabelsErrorComponent | ApiV1S3BucketsCreateNameErrorComponent |
            ApiV1S3BucketsCreateNonFieldErrorsErrorComponent | ApiV1S3BucketsCreateOrganizationErrorComponent |
            ApiV1S3BucketsCreateRegionErrorComponent | ApiV1S3BucketsCreateWorkspaceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1S3BucketsCreateAnnotationsErrorComponent
        | ApiV1S3BucketsCreateCorsAllowAllErrorComponent
        | ApiV1S3BucketsCreateLabelsErrorComponent
        | ApiV1S3BucketsCreateNameErrorComponent
        | ApiV1S3BucketsCreateNonFieldErrorsErrorComponent
        | ApiV1S3BucketsCreateOrganizationErrorComponent
        | ApiV1S3BucketsCreateRegionErrorComponent
        | ApiV1S3BucketsCreateWorkspaceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1s3_buckets_create_annotations_error_component import (
            ApiV1S3BucketsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1s3_buckets_create_labels_error_component import ApiV1S3BucketsCreateLabelsErrorComponent
        from ..models.api_v1s3_buckets_create_name_error_component import ApiV1S3BucketsCreateNameErrorComponent
        from ..models.api_v1s3_buckets_create_non_field_errors_error_component import (
            ApiV1S3BucketsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1s3_buckets_create_organization_error_component import (
            ApiV1S3BucketsCreateOrganizationErrorComponent,
        )
        from ..models.api_v1s3_buckets_create_region_error_component import ApiV1S3BucketsCreateRegionErrorComponent
        from ..models.api_v1s3_buckets_create_workspace_error_component import (
            ApiV1S3BucketsCreateWorkspaceErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1S3BucketsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsCreateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsCreateOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsCreateWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsCreateAnnotationsErrorComponent):
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
        from ..models.api_v1s3_buckets_create_annotations_error_component import (
            ApiV1S3BucketsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1s3_buckets_create_cors_allow_all_error_component import (
            ApiV1S3BucketsCreateCorsAllowAllErrorComponent,
        )
        from ..models.api_v1s3_buckets_create_labels_error_component import ApiV1S3BucketsCreateLabelsErrorComponent
        from ..models.api_v1s3_buckets_create_name_error_component import ApiV1S3BucketsCreateNameErrorComponent
        from ..models.api_v1s3_buckets_create_non_field_errors_error_component import (
            ApiV1S3BucketsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1s3_buckets_create_organization_error_component import (
            ApiV1S3BucketsCreateOrganizationErrorComponent,
        )
        from ..models.api_v1s3_buckets_create_region_error_component import ApiV1S3BucketsCreateRegionErrorComponent
        from ..models.api_v1s3_buckets_create_workspace_error_component import (
            ApiV1S3BucketsCreateWorkspaceErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1S3BucketsCreateAnnotationsErrorComponent
                | ApiV1S3BucketsCreateCorsAllowAllErrorComponent
                | ApiV1S3BucketsCreateLabelsErrorComponent
                | ApiV1S3BucketsCreateNameErrorComponent
                | ApiV1S3BucketsCreateNonFieldErrorsErrorComponent
                | ApiV1S3BucketsCreateOrganizationErrorComponent
                | ApiV1S3BucketsCreateRegionErrorComponent
                | ApiV1S3BucketsCreateWorkspaceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_create_error_type_0 = (
                        ApiV1S3BucketsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_create_error_type_1 = (
                        ApiV1S3BucketsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_create_error_type_2 = (
                        ApiV1S3BucketsCreateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_create_error_type_3 = (
                        ApiV1S3BucketsCreateOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_create_error_type_4 = (
                        ApiV1S3BucketsCreateWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_create_error_type_5 = (
                        ApiV1S3BucketsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_create_error_type_6 = (
                        ApiV1S3BucketsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1s3_buckets_create_error_type_7 = (
                    ApiV1S3BucketsCreateCorsAllowAllErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1s3_buckets_create_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1s3_buckets_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1s3_buckets_create_validation_error.additional_properties = d
        return api_v1s3_buckets_create_validation_error

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
