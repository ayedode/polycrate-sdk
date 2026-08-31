from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_addons_archive_create_actual_availability_error_component import (
        ApiV1KubernetesAddonsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_allow_multiple_error_component import (
        ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_annotations_error_component import (
        ApiV1KubernetesAddonsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_archived_at_error_component import (
        ApiV1KubernetesAddonsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_archived_error_component import (
        ApiV1KubernetesAddonsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_archived_reason_error_component import (
        ApiV1KubernetesAddonsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_block_name_error_component import (
        ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_catalogue_app_error_component import (
        ApiV1KubernetesAddonsArchiveCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_criticality_error_component import (
        ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_debug_mode_error_component import (
        ApiV1KubernetesAddonsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_default_block_config_template_error_component import (
        ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_default_version_error_component import (
        ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_discovery_enabled_error_component import (
        ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_display_name_error_component import (
        ApiV1KubernetesAddonsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_enforcement_error_component import (
        ApiV1KubernetesAddonsArchiveCreateEnforcementErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_is_default_error_component import (
        ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_kind_error_component import (
        ApiV1KubernetesAddonsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_labels_error_component import (
        ApiV1KubernetesAddonsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_name_error_component import (
        ApiV1KubernetesAddonsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_non_field_errors_error_component import (
        ApiV1KubernetesAddonsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_order_error_component import (
        ApiV1KubernetesAddonsArchiveCreateOrderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_platform_service_error_component import (
        ApiV1KubernetesAddonsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_provider_error_component import (
        ApiV1KubernetesAddonsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_provider_id_error_component import (
        ApiV1KubernetesAddonsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_provider_reference_error_component import (
        ApiV1KubernetesAddonsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesAddonsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_scope_error_component import (
        ApiV1KubernetesAddonsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_scope_expressions_error_component import (
        ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_sla_availability_error_component import (
        ApiV1KubernetesAddonsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_sla_target_error_component import (
        ApiV1KubernetesAddonsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_slo_availability_error_component import (
        ApiV1KubernetesAddonsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_slo_target_error_component import (
        ApiV1KubernetesAddonsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_target_availability_error_component import (
        ApiV1KubernetesAddonsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addons_archive_create_template_block_error_component import (
        ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAddonsArchiveCreateValidationError")


@_attrs_define
class ApiV1KubernetesAddonsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAddonsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateAnnotationsErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateArchivedAtErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateArchivedErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateArchivedReasonErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateCatalogueAppErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateDebugModeErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateDisplayNameErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateEnforcementErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponent | ApiV1KubernetesAddonsArchiveCreateKindErrorComponent
            | ApiV1KubernetesAddonsArchiveCreateLabelsErrorComponent | ApiV1KubernetesAddonsArchiveCreateNameErrorComponent
            | ApiV1KubernetesAddonsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateOrderErrorComponent |
            ApiV1KubernetesAddonsArchiveCreatePlatformServiceErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateProviderErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateProviderIdErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateProviderReferenceErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateScopeErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateSlaTargetErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateSloTargetErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAddonsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateAnnotationsErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateArchivedAtErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateArchivedErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateArchivedReasonErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateCatalogueAppErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateDebugModeErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateDisplayNameErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateEnforcementErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateKindErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateLabelsErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateNameErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateOrderErrorComponent
        | ApiV1KubernetesAddonsArchiveCreatePlatformServiceErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateProviderErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateProviderIdErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateProviderReferenceErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateScopeErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateSlaTargetErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateSloTargetErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_addons_archive_create_actual_availability_error_component import (
            ApiV1KubernetesAddonsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_allow_multiple_error_component import (
            ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_annotations_error_component import (
            ApiV1KubernetesAddonsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_archived_at_error_component import (
            ApiV1KubernetesAddonsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_archived_error_component import (
            ApiV1KubernetesAddonsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_archived_reason_error_component import (
            ApiV1KubernetesAddonsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_block_name_error_component import (
            ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_catalogue_app_error_component import (
            ApiV1KubernetesAddonsArchiveCreateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_criticality_error_component import (
            ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_debug_mode_error_component import (
            ApiV1KubernetesAddonsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_default_block_config_template_error_component import (
            ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_default_version_error_component import (
            ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_display_name_error_component import (
            ApiV1KubernetesAddonsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_is_default_error_component import (
            ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_kind_error_component import (
            ApiV1KubernetesAddonsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_labels_error_component import (
            ApiV1KubernetesAddonsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_name_error_component import (
            ApiV1KubernetesAddonsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesAddonsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_order_error_component import (
            ApiV1KubernetesAddonsArchiveCreateOrderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_platform_service_error_component import (
            ApiV1KubernetesAddonsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_provider_error_component import (
            ApiV1KubernetesAddonsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_provider_id_error_component import (
            ApiV1KubernetesAddonsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_provider_reference_error_component import (
            ApiV1KubernetesAddonsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_scope_error_component import (
            ApiV1KubernetesAddonsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_scope_expressions_error_component import (
            ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_sla_availability_error_component import (
            ApiV1KubernetesAddonsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_sla_target_error_component import (
            ApiV1KubernetesAddonsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_slo_availability_error_component import (
            ApiV1KubernetesAddonsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_slo_target_error_component import (
            ApiV1KubernetesAddonsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_target_availability_error_component import (
            ApiV1KubernetesAddonsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_template_block_error_component import (
            ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonsArchiveCreateOrderErrorComponent):
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
        from ..models.api_v1_kubernetes_addons_archive_create_actual_availability_error_component import (
            ApiV1KubernetesAddonsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_allow_multiple_error_component import (
            ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_annotations_error_component import (
            ApiV1KubernetesAddonsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_archived_at_error_component import (
            ApiV1KubernetesAddonsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_archived_error_component import (
            ApiV1KubernetesAddonsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_archived_reason_error_component import (
            ApiV1KubernetesAddonsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_block_name_error_component import (
            ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_catalogue_app_error_component import (
            ApiV1KubernetesAddonsArchiveCreateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_criticality_error_component import (
            ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_debug_mode_error_component import (
            ApiV1KubernetesAddonsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_default_block_config_template_error_component import (
            ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_default_version_error_component import (
            ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_display_name_error_component import (
            ApiV1KubernetesAddonsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_enforcement_error_component import (
            ApiV1KubernetesAddonsArchiveCreateEnforcementErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_is_default_error_component import (
            ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_kind_error_component import (
            ApiV1KubernetesAddonsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_labels_error_component import (
            ApiV1KubernetesAddonsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_name_error_component import (
            ApiV1KubernetesAddonsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesAddonsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_order_error_component import (
            ApiV1KubernetesAddonsArchiveCreateOrderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_platform_service_error_component import (
            ApiV1KubernetesAddonsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_provider_error_component import (
            ApiV1KubernetesAddonsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_provider_id_error_component import (
            ApiV1KubernetesAddonsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_provider_reference_error_component import (
            ApiV1KubernetesAddonsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_scope_error_component import (
            ApiV1KubernetesAddonsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_scope_expressions_error_component import (
            ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_sla_availability_error_component import (
            ApiV1KubernetesAddonsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_sla_target_error_component import (
            ApiV1KubernetesAddonsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_slo_availability_error_component import (
            ApiV1KubernetesAddonsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_slo_target_error_component import (
            ApiV1KubernetesAddonsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_target_availability_error_component import (
            ApiV1KubernetesAddonsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addons_archive_create_template_block_error_component import (
            ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAddonsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateAnnotationsErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateArchivedAtErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateArchivedErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateArchivedReasonErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateCatalogueAppErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateDebugModeErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateDisplayNameErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateEnforcementErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateKindErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateLabelsErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateNameErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateOrderErrorComponent
                | ApiV1KubernetesAddonsArchiveCreatePlatformServiceErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateProviderErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateProviderIdErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateProviderReferenceErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateScopeErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateSlaTargetErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateSloTargetErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_0 = (
                        ApiV1KubernetesAddonsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_1 = (
                        ApiV1KubernetesAddonsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_2 = (
                        ApiV1KubernetesAddonsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_3 = (
                        ApiV1KubernetesAddonsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_4 = (
                        ApiV1KubernetesAddonsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_5 = (
                        ApiV1KubernetesAddonsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_6 = (
                        ApiV1KubernetesAddonsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_7 = (
                        ApiV1KubernetesAddonsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_8 = (
                        ApiV1KubernetesAddonsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_9 = (
                        ApiV1KubernetesAddonsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_10 = (
                        ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_11 = (
                        ApiV1KubernetesAddonsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_12 = (
                        ApiV1KubernetesAddonsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_13 = (
                        ApiV1KubernetesAddonsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_14 = (
                        ApiV1KubernetesAddonsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_15 = (
                        ApiV1KubernetesAddonsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_16 = (
                        ApiV1KubernetesAddonsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_17 = (
                        ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_18 = (
                        ApiV1KubernetesAddonsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_19 = (
                        ApiV1KubernetesAddonsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_20 = (
                        ApiV1KubernetesAddonsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_21 = (
                        ApiV1KubernetesAddonsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_22 = (
                        ApiV1KubernetesAddonsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_23 = (
                        ApiV1KubernetesAddonsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_24 = (
                        ApiV1KubernetesAddonsArchiveCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_25 = (
                        ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_26 = (
                        ApiV1KubernetesAddonsArchiveCreateDefaultVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_27 = (
                        ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_28 = (
                        ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_29 = (
                        ApiV1KubernetesAddonsArchiveCreateScopeExpressionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_30 = (
                        ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_31 = (
                        ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_32 = (
                        ApiV1KubernetesAddonsArchiveCreateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_33 = (
                    ApiV1KubernetesAddonsArchiveCreateEnforcementErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addons_archive_create_error_type_33

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_addons_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_addons_archive_create_validation_error.additional_properties = d
        return api_v1_kubernetes_addons_archive_create_validation_error

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
