from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenance_windows_archive_create_annotations_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_archived_at_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_archived_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_archived_reason_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_criticality_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_debug_mode_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_description_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_display_name_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_is_system_default_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_kind_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_labels_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_lead_time_days_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_name_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_non_field_errors_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_note_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateNoteErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_notice_required_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_platform_service_error_component import (
        ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_provider_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_provider_id_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_provider_reference_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_reconciliation_enabled_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_sla_availability_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_sla_target_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_slo_availability_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_slo_target_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_target_availability_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_time_slots_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateTimeSlotsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_archive_create_tolerations_error_component import (
        ApiV1MaintenanceWindowsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenanceWindowsArchiveCreateValidationError")


@_attrs_define
class ApiV1MaintenanceWindowsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateArchivedAtErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateCriticalityErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateDisplayNameErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateKindErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateLabelsErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateNameErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateNoteErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateProviderErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateProviderIdErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateProviderReferenceErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateSlaTargetErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateTimeSlotsErrorComponent |
            ApiV1MaintenanceWindowsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateArchivedAtErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateCriticalityErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateDisplayNameErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateKindErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateLabelsErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateNameErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateNoteErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateProviderErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateProviderIdErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateProviderReferenceErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateSlaTargetErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateTimeSlotsErrorComponent
        | ApiV1MaintenanceWindowsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenance_windows_archive_create_annotations_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_archived_at_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_archived_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_archived_reason_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_criticality_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_debug_mode_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_description_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_display_name_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_is_system_default_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_kind_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_labels_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_lead_time_days_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_name_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_non_field_errors_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_note_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_notice_required_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_platform_service_error_component import (
            ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_provider_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_provider_id_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_provider_reference_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_reconciliation_enabled_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_sla_availability_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_sla_target_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_slo_availability_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_slo_target_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_target_availability_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_tolerations_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsArchiveCreateNoteErrorComponent):
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
        from ..models.api_v1_maintenance_windows_archive_create_annotations_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_archived_at_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_archived_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_archived_reason_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_criticality_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_debug_mode_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_description_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_display_name_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_is_system_default_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_kind_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_labels_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_lead_time_days_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_name_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_non_field_errors_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_note_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_notice_required_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_platform_service_error_component import (
            ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_provider_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_provider_id_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_provider_reference_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_reconciliation_enabled_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_sla_availability_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_sla_target_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_slo_availability_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_slo_target_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_target_availability_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_time_slots_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateTimeSlotsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_archive_create_tolerations_error_component import (
            ApiV1MaintenanceWindowsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateArchivedAtErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateCriticalityErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateDisplayNameErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateKindErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateLabelsErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateNameErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateNoteErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateProviderErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateProviderIdErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateProviderReferenceErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateSlaTargetErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateTimeSlotsErrorComponent
                | ApiV1MaintenanceWindowsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_0 = (
                        ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_1 = (
                        ApiV1MaintenanceWindowsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_2 = (
                        ApiV1MaintenanceWindowsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_3 = (
                        ApiV1MaintenanceWindowsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_4 = (
                        ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_5 = (
                        ApiV1MaintenanceWindowsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_6 = (
                        ApiV1MaintenanceWindowsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_7 = (
                        ApiV1MaintenanceWindowsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_8 = (
                        ApiV1MaintenanceWindowsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_9 = (
                        ApiV1MaintenanceWindowsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_10 = (
                        ApiV1MaintenanceWindowsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_11 = (
                        ApiV1MaintenanceWindowsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_12 = (
                        ApiV1MaintenanceWindowsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_13 = (
                        ApiV1MaintenanceWindowsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_14 = (
                        ApiV1MaintenanceWindowsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_15 = (
                        ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_16 = (
                        ApiV1MaintenanceWindowsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_17 = (
                        ApiV1MaintenanceWindowsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_18 = (
                        ApiV1MaintenanceWindowsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_19 = (
                        ApiV1MaintenanceWindowsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_20 = (
                        ApiV1MaintenanceWindowsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_21 = (
                        ApiV1MaintenanceWindowsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_22 = (
                        ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_23 = (
                        ApiV1MaintenanceWindowsArchiveCreateLeadTimeDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_24 = (
                        ApiV1MaintenanceWindowsArchiveCreateNoticeRequiredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_25 = (
                        ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_archive_create_error_type_26 = (
                        ApiV1MaintenanceWindowsArchiveCreateNoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenance_windows_archive_create_error_type_27 = (
                    ApiV1MaintenanceWindowsArchiveCreateTimeSlotsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenance_windows_archive_create_error_type_27

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenance_windows_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenance_windows_archive_create_validation_error.additional_properties = d
        return api_v1_maintenance_windows_archive_create_validation_error

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
