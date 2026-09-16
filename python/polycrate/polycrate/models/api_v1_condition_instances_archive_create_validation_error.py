from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_condition_instances_archive_create_active_error_component import (
        ApiV1ConditionInstancesArchiveCreateActiveErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_annotations_error_component import (
        ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_archived_at_error_component import (
        ApiV1ConditionInstancesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_archived_error_component import (
        ApiV1ConditionInstancesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_archived_reason_error_component import (
        ApiV1ConditionInstancesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_condition_error_component import (
        ApiV1ConditionInstancesArchiveCreateConditionErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_context_error_component import (
        ApiV1ConditionInstancesArchiveCreateContextErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_criticality_error_component import (
        ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_debug_mode_error_component import (
        ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_display_name_error_component import (
        ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_immediate_error_component import (
        ApiV1ConditionInstancesArchiveCreateImmediateErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_kind_error_component import (
        ApiV1ConditionInstancesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_labels_error_component import (
        ApiV1ConditionInstancesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_name_error_component import (
        ApiV1ConditionInstancesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_non_field_errors_error_component import (
        ApiV1ConditionInstancesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_object_id_error_component import (
        ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_platform_service_error_component import (
        ApiV1ConditionInstancesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_provider_error_component import (
        ApiV1ConditionInstancesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_provider_id_error_component import (
        ApiV1ConditionInstancesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_provider_reference_error_component import (
        ApiV1ConditionInstancesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_reason_error_component import (
        ApiV1ConditionInstancesArchiveCreateReasonErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_reconciliation_enabled_error_component import (
        ApiV1ConditionInstancesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_resolved_at_error_component import (
        ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_sla_availability_error_component import (
        ApiV1ConditionInstancesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_sla_target_error_component import (
        ApiV1ConditionInstancesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_slo_availability_error_component import (
        ApiV1ConditionInstancesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_slo_target_error_component import (
        ApiV1ConditionInstancesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_target_availability_error_component import (
        ApiV1ConditionInstancesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_archive_create_tolerations_error_component import (
        ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConditionInstancesArchiveCreateValidationError")


@_attrs_define
class ApiV1ConditionInstancesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConditionInstancesArchiveCreateActiveErrorComponent |
            ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponent |
            ApiV1ConditionInstancesArchiveCreateArchivedAtErrorComponent |
            ApiV1ConditionInstancesArchiveCreateArchivedErrorComponent |
            ApiV1ConditionInstancesArchiveCreateArchivedReasonErrorComponent |
            ApiV1ConditionInstancesArchiveCreateConditionErrorComponent |
            ApiV1ConditionInstancesArchiveCreateContextErrorComponent |
            ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponent |
            ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponent |
            ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponent |
            ApiV1ConditionInstancesArchiveCreateImmediateErrorComponent |
            ApiV1ConditionInstancesArchiveCreateKindErrorComponent |
            ApiV1ConditionInstancesArchiveCreateLabelsErrorComponent |
            ApiV1ConditionInstancesArchiveCreateNameErrorComponent |
            ApiV1ConditionInstancesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponent |
            ApiV1ConditionInstancesArchiveCreatePlatformServiceErrorComponent |
            ApiV1ConditionInstancesArchiveCreateProviderErrorComponent |
            ApiV1ConditionInstancesArchiveCreateProviderIdErrorComponent |
            ApiV1ConditionInstancesArchiveCreateProviderReferenceErrorComponent |
            ApiV1ConditionInstancesArchiveCreateReasonErrorComponent |
            ApiV1ConditionInstancesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponent |
            ApiV1ConditionInstancesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1ConditionInstancesArchiveCreateSlaTargetErrorComponent |
            ApiV1ConditionInstancesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1ConditionInstancesArchiveCreateSloTargetErrorComponent |
            ApiV1ConditionInstancesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConditionInstancesArchiveCreateActiveErrorComponent
        | ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponent
        | ApiV1ConditionInstancesArchiveCreateArchivedAtErrorComponent
        | ApiV1ConditionInstancesArchiveCreateArchivedErrorComponent
        | ApiV1ConditionInstancesArchiveCreateArchivedReasonErrorComponent
        | ApiV1ConditionInstancesArchiveCreateConditionErrorComponent
        | ApiV1ConditionInstancesArchiveCreateContextErrorComponent
        | ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponent
        | ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponent
        | ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponent
        | ApiV1ConditionInstancesArchiveCreateImmediateErrorComponent
        | ApiV1ConditionInstancesArchiveCreateKindErrorComponent
        | ApiV1ConditionInstancesArchiveCreateLabelsErrorComponent
        | ApiV1ConditionInstancesArchiveCreateNameErrorComponent
        | ApiV1ConditionInstancesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponent
        | ApiV1ConditionInstancesArchiveCreatePlatformServiceErrorComponent
        | ApiV1ConditionInstancesArchiveCreateProviderErrorComponent
        | ApiV1ConditionInstancesArchiveCreateProviderIdErrorComponent
        | ApiV1ConditionInstancesArchiveCreateProviderReferenceErrorComponent
        | ApiV1ConditionInstancesArchiveCreateReasonErrorComponent
        | ApiV1ConditionInstancesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponent
        | ApiV1ConditionInstancesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1ConditionInstancesArchiveCreateSlaTargetErrorComponent
        | ApiV1ConditionInstancesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1ConditionInstancesArchiveCreateSloTargetErrorComponent
        | ApiV1ConditionInstancesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_condition_instances_archive_create_active_error_component import (
            ApiV1ConditionInstancesArchiveCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_annotations_error_component import (
            ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_archived_at_error_component import (
            ApiV1ConditionInstancesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_archived_error_component import (
            ApiV1ConditionInstancesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_archived_reason_error_component import (
            ApiV1ConditionInstancesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_condition_error_component import (
            ApiV1ConditionInstancesArchiveCreateConditionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_context_error_component import (
            ApiV1ConditionInstancesArchiveCreateContextErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_criticality_error_component import (
            ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_debug_mode_error_component import (
            ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_display_name_error_component import (
            ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_immediate_error_component import (
            ApiV1ConditionInstancesArchiveCreateImmediateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_kind_error_component import (
            ApiV1ConditionInstancesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_labels_error_component import (
            ApiV1ConditionInstancesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_name_error_component import (
            ApiV1ConditionInstancesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_non_field_errors_error_component import (
            ApiV1ConditionInstancesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_object_id_error_component import (
            ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_platform_service_error_component import (
            ApiV1ConditionInstancesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_provider_error_component import (
            ApiV1ConditionInstancesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_provider_id_error_component import (
            ApiV1ConditionInstancesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_provider_reference_error_component import (
            ApiV1ConditionInstancesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_reason_error_component import (
            ApiV1ConditionInstancesArchiveCreateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_reconciliation_enabled_error_component import (
            ApiV1ConditionInstancesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_sla_availability_error_component import (
            ApiV1ConditionInstancesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_sla_target_error_component import (
            ApiV1ConditionInstancesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_slo_availability_error_component import (
            ApiV1ConditionInstancesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_slo_target_error_component import (
            ApiV1ConditionInstancesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_target_availability_error_component import (
            ApiV1ConditionInstancesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_tolerations_error_component import (
            ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateConditionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateContextErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateImmediateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesArchiveCreateActiveErrorComponent):
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
        from ..models.api_v1_condition_instances_archive_create_active_error_component import (
            ApiV1ConditionInstancesArchiveCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_annotations_error_component import (
            ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_archived_at_error_component import (
            ApiV1ConditionInstancesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_archived_error_component import (
            ApiV1ConditionInstancesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_archived_reason_error_component import (
            ApiV1ConditionInstancesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_condition_error_component import (
            ApiV1ConditionInstancesArchiveCreateConditionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_context_error_component import (
            ApiV1ConditionInstancesArchiveCreateContextErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_criticality_error_component import (
            ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_debug_mode_error_component import (
            ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_display_name_error_component import (
            ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_immediate_error_component import (
            ApiV1ConditionInstancesArchiveCreateImmediateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_kind_error_component import (
            ApiV1ConditionInstancesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_labels_error_component import (
            ApiV1ConditionInstancesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_name_error_component import (
            ApiV1ConditionInstancesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_non_field_errors_error_component import (
            ApiV1ConditionInstancesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_object_id_error_component import (
            ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_platform_service_error_component import (
            ApiV1ConditionInstancesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_provider_error_component import (
            ApiV1ConditionInstancesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_provider_id_error_component import (
            ApiV1ConditionInstancesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_provider_reference_error_component import (
            ApiV1ConditionInstancesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_reason_error_component import (
            ApiV1ConditionInstancesArchiveCreateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_reconciliation_enabled_error_component import (
            ApiV1ConditionInstancesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_resolved_at_error_component import (
            ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_sla_availability_error_component import (
            ApiV1ConditionInstancesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_sla_target_error_component import (
            ApiV1ConditionInstancesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_slo_availability_error_component import (
            ApiV1ConditionInstancesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_slo_target_error_component import (
            ApiV1ConditionInstancesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_target_availability_error_component import (
            ApiV1ConditionInstancesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_condition_instances_archive_create_tolerations_error_component import (
            ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConditionInstancesArchiveCreateActiveErrorComponent
                | ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponent
                | ApiV1ConditionInstancesArchiveCreateArchivedAtErrorComponent
                | ApiV1ConditionInstancesArchiveCreateArchivedErrorComponent
                | ApiV1ConditionInstancesArchiveCreateArchivedReasonErrorComponent
                | ApiV1ConditionInstancesArchiveCreateConditionErrorComponent
                | ApiV1ConditionInstancesArchiveCreateContextErrorComponent
                | ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponent
                | ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponent
                | ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponent
                | ApiV1ConditionInstancesArchiveCreateImmediateErrorComponent
                | ApiV1ConditionInstancesArchiveCreateKindErrorComponent
                | ApiV1ConditionInstancesArchiveCreateLabelsErrorComponent
                | ApiV1ConditionInstancesArchiveCreateNameErrorComponent
                | ApiV1ConditionInstancesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponent
                | ApiV1ConditionInstancesArchiveCreatePlatformServiceErrorComponent
                | ApiV1ConditionInstancesArchiveCreateProviderErrorComponent
                | ApiV1ConditionInstancesArchiveCreateProviderIdErrorComponent
                | ApiV1ConditionInstancesArchiveCreateProviderReferenceErrorComponent
                | ApiV1ConditionInstancesArchiveCreateReasonErrorComponent
                | ApiV1ConditionInstancesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponent
                | ApiV1ConditionInstancesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1ConditionInstancesArchiveCreateSlaTargetErrorComponent
                | ApiV1ConditionInstancesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1ConditionInstancesArchiveCreateSloTargetErrorComponent
                | ApiV1ConditionInstancesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_0 = (
                        ApiV1ConditionInstancesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_1 = (
                        ApiV1ConditionInstancesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_2 = (
                        ApiV1ConditionInstancesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_3 = (
                        ApiV1ConditionInstancesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_4 = (
                        ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_5 = (
                        ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_6 = (
                        ApiV1ConditionInstancesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_7 = (
                        ApiV1ConditionInstancesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_8 = (
                        ApiV1ConditionInstancesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_9 = (
                        ApiV1ConditionInstancesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_10 = (
                        ApiV1ConditionInstancesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_11 = (
                        ApiV1ConditionInstancesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_12 = (
                        ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_13 = (
                        ApiV1ConditionInstancesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_14 = (
                        ApiV1ConditionInstancesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_15 = (
                        ApiV1ConditionInstancesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_16 = (
                        ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_17 = (
                        ApiV1ConditionInstancesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_18 = (
                        ApiV1ConditionInstancesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_19 = (
                        ApiV1ConditionInstancesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_20 = (
                        ApiV1ConditionInstancesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_21 = (
                        ApiV1ConditionInstancesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_22 = (
                        ApiV1ConditionInstancesArchiveCreateConditionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_23 = (
                        ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_24 = (
                        ApiV1ConditionInstancesArchiveCreateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_25 = (
                        ApiV1ConditionInstancesArchiveCreateContextErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_26 = (
                        ApiV1ConditionInstancesArchiveCreateImmediateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_archive_create_error_type_27 = (
                        ApiV1ConditionInstancesArchiveCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_condition_instances_archive_create_error_type_28 = (
                    ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_condition_instances_archive_create_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_condition_instances_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_condition_instances_archive_create_validation_error.additional_properties = d
        return api_v1_condition_instances_archive_create_validation_error

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
