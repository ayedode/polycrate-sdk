from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1s3_buckets_archive_create_annotations_error_component import (
        ApiV1S3BucketsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_archived_at_error_component import (
        ApiV1S3BucketsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_archived_error_component import (
        ApiV1S3BucketsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_archived_reason_error_component import (
        ApiV1S3BucketsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_cors_allow_all_error_component import (
        ApiV1S3BucketsArchiveCreateCorsAllowAllErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_criticality_error_component import (
        ApiV1S3BucketsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_debug_mode_error_component import (
        ApiV1S3BucketsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_display_name_error_component import (
        ApiV1S3BucketsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_include_in_cost_statement_error_component import (
        ApiV1S3BucketsArchiveCreateIncludeInCostStatementErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_kind_error_component import (
        ApiV1S3BucketsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_labels_error_component import (
        ApiV1S3BucketsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_name_error_component import (
        ApiV1S3BucketsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_non_field_errors_error_component import (
        ApiV1S3BucketsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_platform_service_error_component import (
        ApiV1S3BucketsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_provider_error_component import (
        ApiV1S3BucketsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_provider_id_error_component import (
        ApiV1S3BucketsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_provider_reference_error_component import (
        ApiV1S3BucketsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_reconciliation_enabled_error_component import (
        ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_sla_availability_error_component import (
        ApiV1S3BucketsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_sla_target_error_component import (
        ApiV1S3BucketsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_slo_availability_error_component import (
        ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_slo_target_error_component import (
        ApiV1S3BucketsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_target_availability_error_component import (
        ApiV1S3BucketsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_buckets_archive_create_tolerations_error_component import (
        ApiV1S3BucketsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1S3BucketsArchiveCreateValidationError")


@_attrs_define
class ApiV1S3BucketsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1S3BucketsArchiveCreateAnnotationsErrorComponent |
            ApiV1S3BucketsArchiveCreateArchivedAtErrorComponent | ApiV1S3BucketsArchiveCreateArchivedErrorComponent |
            ApiV1S3BucketsArchiveCreateArchivedReasonErrorComponent | ApiV1S3BucketsArchiveCreateCorsAllowAllErrorComponent
            | ApiV1S3BucketsArchiveCreateCriticalityErrorComponent | ApiV1S3BucketsArchiveCreateDebugModeErrorComponent |
            ApiV1S3BucketsArchiveCreateDisplayNameErrorComponent |
            ApiV1S3BucketsArchiveCreateIncludeInCostStatementErrorComponent | ApiV1S3BucketsArchiveCreateKindErrorComponent
            | ApiV1S3BucketsArchiveCreateLabelsErrorComponent | ApiV1S3BucketsArchiveCreateNameErrorComponent |
            ApiV1S3BucketsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1S3BucketsArchiveCreatePlatformServiceErrorComponent | ApiV1S3BucketsArchiveCreateProviderErrorComponent |
            ApiV1S3BucketsArchiveCreateProviderIdErrorComponent | ApiV1S3BucketsArchiveCreateProviderReferenceErrorComponent
            | ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1S3BucketsArchiveCreateSlaAvailabilityErrorComponent | ApiV1S3BucketsArchiveCreateSlaTargetErrorComponent |
            ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponent | ApiV1S3BucketsArchiveCreateSloTargetErrorComponent |
            ApiV1S3BucketsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1S3BucketsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1S3BucketsArchiveCreateAnnotationsErrorComponent
        | ApiV1S3BucketsArchiveCreateArchivedAtErrorComponent
        | ApiV1S3BucketsArchiveCreateArchivedErrorComponent
        | ApiV1S3BucketsArchiveCreateArchivedReasonErrorComponent
        | ApiV1S3BucketsArchiveCreateCorsAllowAllErrorComponent
        | ApiV1S3BucketsArchiveCreateCriticalityErrorComponent
        | ApiV1S3BucketsArchiveCreateDebugModeErrorComponent
        | ApiV1S3BucketsArchiveCreateDisplayNameErrorComponent
        | ApiV1S3BucketsArchiveCreateIncludeInCostStatementErrorComponent
        | ApiV1S3BucketsArchiveCreateKindErrorComponent
        | ApiV1S3BucketsArchiveCreateLabelsErrorComponent
        | ApiV1S3BucketsArchiveCreateNameErrorComponent
        | ApiV1S3BucketsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1S3BucketsArchiveCreatePlatformServiceErrorComponent
        | ApiV1S3BucketsArchiveCreateProviderErrorComponent
        | ApiV1S3BucketsArchiveCreateProviderIdErrorComponent
        | ApiV1S3BucketsArchiveCreateProviderReferenceErrorComponent
        | ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1S3BucketsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1S3BucketsArchiveCreateSlaTargetErrorComponent
        | ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1S3BucketsArchiveCreateSloTargetErrorComponent
        | ApiV1S3BucketsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1S3BucketsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1s3_buckets_archive_create_annotations_error_component import (
            ApiV1S3BucketsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_archived_at_error_component import (
            ApiV1S3BucketsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_archived_error_component import (
            ApiV1S3BucketsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_archived_reason_error_component import (
            ApiV1S3BucketsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_criticality_error_component import (
            ApiV1S3BucketsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_debug_mode_error_component import (
            ApiV1S3BucketsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_display_name_error_component import (
            ApiV1S3BucketsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_include_in_cost_statement_error_component import (
            ApiV1S3BucketsArchiveCreateIncludeInCostStatementErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_kind_error_component import (
            ApiV1S3BucketsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_labels_error_component import (
            ApiV1S3BucketsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_name_error_component import (
            ApiV1S3BucketsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_non_field_errors_error_component import (
            ApiV1S3BucketsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_platform_service_error_component import (
            ApiV1S3BucketsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_provider_error_component import (
            ApiV1S3BucketsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_provider_id_error_component import (
            ApiV1S3BucketsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_provider_reference_error_component import (
            ApiV1S3BucketsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_reconciliation_enabled_error_component import (
            ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_sla_availability_error_component import (
            ApiV1S3BucketsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_sla_target_error_component import (
            ApiV1S3BucketsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_slo_availability_error_component import (
            ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_slo_target_error_component import (
            ApiV1S3BucketsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_target_availability_error_component import (
            ApiV1S3BucketsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_tolerations_error_component import (
            ApiV1S3BucketsArchiveCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3BucketsArchiveCreateIncludeInCostStatementErrorComponent):
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
        from ..models.api_v1s3_buckets_archive_create_annotations_error_component import (
            ApiV1S3BucketsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_archived_at_error_component import (
            ApiV1S3BucketsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_archived_error_component import (
            ApiV1S3BucketsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_archived_reason_error_component import (
            ApiV1S3BucketsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_cors_allow_all_error_component import (
            ApiV1S3BucketsArchiveCreateCorsAllowAllErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_criticality_error_component import (
            ApiV1S3BucketsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_debug_mode_error_component import (
            ApiV1S3BucketsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_display_name_error_component import (
            ApiV1S3BucketsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_include_in_cost_statement_error_component import (
            ApiV1S3BucketsArchiveCreateIncludeInCostStatementErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_kind_error_component import (
            ApiV1S3BucketsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_labels_error_component import (
            ApiV1S3BucketsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_name_error_component import (
            ApiV1S3BucketsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_non_field_errors_error_component import (
            ApiV1S3BucketsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_platform_service_error_component import (
            ApiV1S3BucketsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_provider_error_component import (
            ApiV1S3BucketsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_provider_id_error_component import (
            ApiV1S3BucketsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_provider_reference_error_component import (
            ApiV1S3BucketsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_reconciliation_enabled_error_component import (
            ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_sla_availability_error_component import (
            ApiV1S3BucketsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_sla_target_error_component import (
            ApiV1S3BucketsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_slo_availability_error_component import (
            ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_slo_target_error_component import (
            ApiV1S3BucketsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_target_availability_error_component import (
            ApiV1S3BucketsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_buckets_archive_create_tolerations_error_component import (
            ApiV1S3BucketsArchiveCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1S3BucketsArchiveCreateAnnotationsErrorComponent
                | ApiV1S3BucketsArchiveCreateArchivedAtErrorComponent
                | ApiV1S3BucketsArchiveCreateArchivedErrorComponent
                | ApiV1S3BucketsArchiveCreateArchivedReasonErrorComponent
                | ApiV1S3BucketsArchiveCreateCorsAllowAllErrorComponent
                | ApiV1S3BucketsArchiveCreateCriticalityErrorComponent
                | ApiV1S3BucketsArchiveCreateDebugModeErrorComponent
                | ApiV1S3BucketsArchiveCreateDisplayNameErrorComponent
                | ApiV1S3BucketsArchiveCreateIncludeInCostStatementErrorComponent
                | ApiV1S3BucketsArchiveCreateKindErrorComponent
                | ApiV1S3BucketsArchiveCreateLabelsErrorComponent
                | ApiV1S3BucketsArchiveCreateNameErrorComponent
                | ApiV1S3BucketsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1S3BucketsArchiveCreatePlatformServiceErrorComponent
                | ApiV1S3BucketsArchiveCreateProviderErrorComponent
                | ApiV1S3BucketsArchiveCreateProviderIdErrorComponent
                | ApiV1S3BucketsArchiveCreateProviderReferenceErrorComponent
                | ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1S3BucketsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1S3BucketsArchiveCreateSlaTargetErrorComponent
                | ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1S3BucketsArchiveCreateSloTargetErrorComponent
                | ApiV1S3BucketsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1S3BucketsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_0 = (
                        ApiV1S3BucketsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_1 = (
                        ApiV1S3BucketsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_2 = (
                        ApiV1S3BucketsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_3 = (
                        ApiV1S3BucketsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_4 = (
                        ApiV1S3BucketsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_5 = (
                        ApiV1S3BucketsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_6 = (
                        ApiV1S3BucketsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_7 = (
                        ApiV1S3BucketsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_8 = (
                        ApiV1S3BucketsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_9 = (
                        ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_10 = (
                        ApiV1S3BucketsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_11 = (
                        ApiV1S3BucketsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_12 = (
                        ApiV1S3BucketsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_13 = (
                        ApiV1S3BucketsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_14 = (
                        ApiV1S3BucketsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_15 = (
                        ApiV1S3BucketsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_16 = (
                        ApiV1S3BucketsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_17 = (
                        ApiV1S3BucketsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_18 = (
                        ApiV1S3BucketsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_19 = (
                        ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_20 = (
                        ApiV1S3BucketsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_21 = (
                        ApiV1S3BucketsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_buckets_archive_create_error_type_22 = (
                        ApiV1S3BucketsArchiveCreateIncludeInCostStatementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_buckets_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1s3_buckets_archive_create_error_type_23 = (
                    ApiV1S3BucketsArchiveCreateCorsAllowAllErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1s3_buckets_archive_create_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1s3_buckets_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1s3_buckets_archive_create_validation_error.additional_properties = d
        return api_v1s3_buckets_archive_create_validation_error

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
