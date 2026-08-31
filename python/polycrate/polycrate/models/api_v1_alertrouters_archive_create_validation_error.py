from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alertrouters_archive_create_annotations_error_component import (
        ApiV1AlertroutersArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_archived_at_error_component import (
        ApiV1AlertroutersArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_archived_error_component import (
        ApiV1AlertroutersArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_archived_reason_error_component import (
        ApiV1AlertroutersArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_criticality_error_component import (
        ApiV1AlertroutersArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_debug_mode_error_component import (
        ApiV1AlertroutersArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_display_name_error_component import (
        ApiV1AlertroutersArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_kind_error_component import (
        ApiV1AlertroutersArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_label_cluster_error_component import (
        ApiV1AlertroutersArchiveCreateLabelClusterErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_label_criticality_error_component import (
        ApiV1AlertroutersArchiveCreateLabelCriticalityErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_label_namespace_error_component import (
        ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_label_organization_error_component import (
        ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_label_pod_error_component import (
        ApiV1AlertroutersArchiveCreateLabelPodErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_label_workspace_error_component import (
        ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_labels_error_component import (
        ApiV1AlertroutersArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_name_error_component import (
        ApiV1AlertroutersArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_non_field_errors_error_component import (
        ApiV1AlertroutersArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_organization_id_error_component import (
        ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_platform_service_error_component import (
        ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_provider_error_component import (
        ApiV1AlertroutersArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_provider_id_error_component import (
        ApiV1AlertroutersArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_provider_reference_error_component import (
        ApiV1AlertroutersArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_reconciliation_enabled_error_component import (
        ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_sla_availability_error_component import (
        ApiV1AlertroutersArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_sla_target_error_component import (
        ApiV1AlertroutersArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_slo_availability_error_component import (
        ApiV1AlertroutersArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_slo_target_error_component import (
        ApiV1AlertroutersArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_target_availability_error_component import (
        ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_tolerations_error_component import (
        ApiV1AlertroutersArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_alertrouters_archive_create_workspace_id_error_component import (
        ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertroutersArchiveCreateValidationError")


@_attrs_define
class ApiV1AlertroutersArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertroutersArchiveCreateAnnotationsErrorComponent |
            ApiV1AlertroutersArchiveCreateArchivedAtErrorComponent | ApiV1AlertroutersArchiveCreateArchivedErrorComponent |
            ApiV1AlertroutersArchiveCreateArchivedReasonErrorComponent |
            ApiV1AlertroutersArchiveCreateCriticalityErrorComponent | ApiV1AlertroutersArchiveCreateDebugModeErrorComponent
            | ApiV1AlertroutersArchiveCreateDisplayNameErrorComponent | ApiV1AlertroutersArchiveCreateKindErrorComponent |
            ApiV1AlertroutersArchiveCreateLabelClusterErrorComponent |
            ApiV1AlertroutersArchiveCreateLabelCriticalityErrorComponent |
            ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponent |
            ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponent |
            ApiV1AlertroutersArchiveCreateLabelPodErrorComponent | ApiV1AlertroutersArchiveCreateLabelsErrorComponent |
            ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponent | ApiV1AlertroutersArchiveCreateNameErrorComponent |
            ApiV1AlertroutersArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponent |
            ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponent |
            ApiV1AlertroutersArchiveCreateProviderErrorComponent | ApiV1AlertroutersArchiveCreateProviderIdErrorComponent |
            ApiV1AlertroutersArchiveCreateProviderReferenceErrorComponent |
            ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1AlertroutersArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1AlertroutersArchiveCreateSlaTargetErrorComponent |
            ApiV1AlertroutersArchiveCreateSloAvailabilityErrorComponent |
            ApiV1AlertroutersArchiveCreateSloTargetErrorComponent |
            ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1AlertroutersArchiveCreateTolerationsErrorComponent |
            ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertroutersArchiveCreateAnnotationsErrorComponent
        | ApiV1AlertroutersArchiveCreateArchivedAtErrorComponent
        | ApiV1AlertroutersArchiveCreateArchivedErrorComponent
        | ApiV1AlertroutersArchiveCreateArchivedReasonErrorComponent
        | ApiV1AlertroutersArchiveCreateCriticalityErrorComponent
        | ApiV1AlertroutersArchiveCreateDebugModeErrorComponent
        | ApiV1AlertroutersArchiveCreateDisplayNameErrorComponent
        | ApiV1AlertroutersArchiveCreateKindErrorComponent
        | ApiV1AlertroutersArchiveCreateLabelClusterErrorComponent
        | ApiV1AlertroutersArchiveCreateLabelCriticalityErrorComponent
        | ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponent
        | ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponent
        | ApiV1AlertroutersArchiveCreateLabelPodErrorComponent
        | ApiV1AlertroutersArchiveCreateLabelsErrorComponent
        | ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponent
        | ApiV1AlertroutersArchiveCreateNameErrorComponent
        | ApiV1AlertroutersArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponent
        | ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponent
        | ApiV1AlertroutersArchiveCreateProviderErrorComponent
        | ApiV1AlertroutersArchiveCreateProviderIdErrorComponent
        | ApiV1AlertroutersArchiveCreateProviderReferenceErrorComponent
        | ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1AlertroutersArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1AlertroutersArchiveCreateSlaTargetErrorComponent
        | ApiV1AlertroutersArchiveCreateSloAvailabilityErrorComponent
        | ApiV1AlertroutersArchiveCreateSloTargetErrorComponent
        | ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1AlertroutersArchiveCreateTolerationsErrorComponent
        | ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alertrouters_archive_create_annotations_error_component import (
            ApiV1AlertroutersArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_archived_at_error_component import (
            ApiV1AlertroutersArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_archived_error_component import (
            ApiV1AlertroutersArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_archived_reason_error_component import (
            ApiV1AlertroutersArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_criticality_error_component import (
            ApiV1AlertroutersArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_debug_mode_error_component import (
            ApiV1AlertroutersArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_display_name_error_component import (
            ApiV1AlertroutersArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_kind_error_component import (
            ApiV1AlertroutersArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_cluster_error_component import (
            ApiV1AlertroutersArchiveCreateLabelClusterErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_namespace_error_component import (
            ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_organization_error_component import (
            ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_pod_error_component import (
            ApiV1AlertroutersArchiveCreateLabelPodErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_workspace_error_component import (
            ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_labels_error_component import (
            ApiV1AlertroutersArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_name_error_component import (
            ApiV1AlertroutersArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_non_field_errors_error_component import (
            ApiV1AlertroutersArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_organization_id_error_component import (
            ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_platform_service_error_component import (
            ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_provider_error_component import (
            ApiV1AlertroutersArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_provider_id_error_component import (
            ApiV1AlertroutersArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_provider_reference_error_component import (
            ApiV1AlertroutersArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_reconciliation_enabled_error_component import (
            ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_sla_availability_error_component import (
            ApiV1AlertroutersArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_sla_target_error_component import (
            ApiV1AlertroutersArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_slo_availability_error_component import (
            ApiV1AlertroutersArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_slo_target_error_component import (
            ApiV1AlertroutersArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_target_availability_error_component import (
            ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_tolerations_error_component import (
            ApiV1AlertroutersArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_workspace_id_error_component import (
            ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateLabelClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateLabelPodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponent):
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
        from ..models.api_v1_alertrouters_archive_create_annotations_error_component import (
            ApiV1AlertroutersArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_archived_at_error_component import (
            ApiV1AlertroutersArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_archived_error_component import (
            ApiV1AlertroutersArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_archived_reason_error_component import (
            ApiV1AlertroutersArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_criticality_error_component import (
            ApiV1AlertroutersArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_debug_mode_error_component import (
            ApiV1AlertroutersArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_display_name_error_component import (
            ApiV1AlertroutersArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_kind_error_component import (
            ApiV1AlertroutersArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_cluster_error_component import (
            ApiV1AlertroutersArchiveCreateLabelClusterErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_criticality_error_component import (
            ApiV1AlertroutersArchiveCreateLabelCriticalityErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_namespace_error_component import (
            ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_organization_error_component import (
            ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_pod_error_component import (
            ApiV1AlertroutersArchiveCreateLabelPodErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_label_workspace_error_component import (
            ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_labels_error_component import (
            ApiV1AlertroutersArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_name_error_component import (
            ApiV1AlertroutersArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_non_field_errors_error_component import (
            ApiV1AlertroutersArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_organization_id_error_component import (
            ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_platform_service_error_component import (
            ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_provider_error_component import (
            ApiV1AlertroutersArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_provider_id_error_component import (
            ApiV1AlertroutersArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_provider_reference_error_component import (
            ApiV1AlertroutersArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_reconciliation_enabled_error_component import (
            ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_sla_availability_error_component import (
            ApiV1AlertroutersArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_sla_target_error_component import (
            ApiV1AlertroutersArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_slo_availability_error_component import (
            ApiV1AlertroutersArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_slo_target_error_component import (
            ApiV1AlertroutersArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_target_availability_error_component import (
            ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_tolerations_error_component import (
            ApiV1AlertroutersArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_archive_create_workspace_id_error_component import (
            ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertroutersArchiveCreateAnnotationsErrorComponent
                | ApiV1AlertroutersArchiveCreateArchivedAtErrorComponent
                | ApiV1AlertroutersArchiveCreateArchivedErrorComponent
                | ApiV1AlertroutersArchiveCreateArchivedReasonErrorComponent
                | ApiV1AlertroutersArchiveCreateCriticalityErrorComponent
                | ApiV1AlertroutersArchiveCreateDebugModeErrorComponent
                | ApiV1AlertroutersArchiveCreateDisplayNameErrorComponent
                | ApiV1AlertroutersArchiveCreateKindErrorComponent
                | ApiV1AlertroutersArchiveCreateLabelClusterErrorComponent
                | ApiV1AlertroutersArchiveCreateLabelCriticalityErrorComponent
                | ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponent
                | ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponent
                | ApiV1AlertroutersArchiveCreateLabelPodErrorComponent
                | ApiV1AlertroutersArchiveCreateLabelsErrorComponent
                | ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponent
                | ApiV1AlertroutersArchiveCreateNameErrorComponent
                | ApiV1AlertroutersArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponent
                | ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponent
                | ApiV1AlertroutersArchiveCreateProviderErrorComponent
                | ApiV1AlertroutersArchiveCreateProviderIdErrorComponent
                | ApiV1AlertroutersArchiveCreateProviderReferenceErrorComponent
                | ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1AlertroutersArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1AlertroutersArchiveCreateSlaTargetErrorComponent
                | ApiV1AlertroutersArchiveCreateSloAvailabilityErrorComponent
                | ApiV1AlertroutersArchiveCreateSloTargetErrorComponent
                | ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1AlertroutersArchiveCreateTolerationsErrorComponent
                | ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_0 = (
                        ApiV1AlertroutersArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_1 = (
                        ApiV1AlertroutersArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_2 = (
                        ApiV1AlertroutersArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_3 = (
                        ApiV1AlertroutersArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_4 = (
                        ApiV1AlertroutersArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_5 = (
                        ApiV1AlertroutersArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_6 = (
                        ApiV1AlertroutersArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_7 = (
                        ApiV1AlertroutersArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_8 = (
                        ApiV1AlertroutersArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_9 = (
                        ApiV1AlertroutersArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_10 = (
                        ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_11 = (
                        ApiV1AlertroutersArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_12 = (
                        ApiV1AlertroutersArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_13 = (
                        ApiV1AlertroutersArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_14 = (
                        ApiV1AlertroutersArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_15 = (
                        ApiV1AlertroutersArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_16 = (
                        ApiV1AlertroutersArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_17 = (
                        ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_18 = (
                        ApiV1AlertroutersArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_19 = (
                        ApiV1AlertroutersArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_20 = (
                        ApiV1AlertroutersArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_21 = (
                        ApiV1AlertroutersArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_22 = (
                        ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_23 = (
                        ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_24 = (
                        ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_25 = (
                        ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_26 = (
                        ApiV1AlertroutersArchiveCreateLabelClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_27 = (
                        ApiV1AlertroutersArchiveCreateLabelPodErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_archive_create_error_type_28 = (
                        ApiV1AlertroutersArchiveCreateLabelNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertrouters_archive_create_error_type_29 = (
                    ApiV1AlertroutersArchiveCreateLabelCriticalityErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alertrouters_archive_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alertrouters_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alertrouters_archive_create_validation_error.additional_properties = d
        return api_v1_alertrouters_archive_create_validation_error

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
